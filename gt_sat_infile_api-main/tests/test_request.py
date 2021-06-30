"""Tests"""
from xml.etree import ElementTree as ET

from gt_sat_api.parsers import dte_to_xml

from gt_sat_infile_api.login import LoginHandler
from gt_sat_infile_api.parser import generate_and_parse_query


def test_generate_query(xml_example):
    """Test a correct generation and response of DTE"""
    auth_headers = LoginHandler(
        user_sign="ASTECK",
        sign_key="cba1f67cb3ffc350489108c08f92fba3",
        user_api="ASTECK",
        api_key="7C7A187E9E8450B1F7812C7D6225A6AA",
    )
    result = generate_and_parse_query(
        auth_headers=auth_headers,
        identifier="123",
        xml=xml_example,
    )
    assert result["res"]
    assert result["xml"]
    assert result["date_certificate"]
    assert result["uuid"]
    assert result["series"]
    assert result["number"]
    assert ET.fromstring(result["xml"])


def test_generate_query_false_auth(xml_example):
    """Test a incorrect generation and response of DTE
    by sending a false authentication
    """
    auth_headers = LoginHandler(
        user_sign="ASTECK",
        sign_key="7C7A187E9E8450B1F7812C7D6225A6AA",
        user_api="ASTECK",
        api_key="cba1f67cb3ffc350489108c08f92fba3",
    )
    result = generate_and_parse_query(
        auth_headers=auth_headers,
        identifier="123",
        xml=xml_example,
    )
    expected_error = {
        "resultado": False,
        "fuente": "Firma Digital del Emisor",
        "categoria": "1",
        "numeral": "1",
        "validacion": "1",
        "mensaje_error": "Firma no encontrado, o pendiente de aprobar",
    }
    assert not result["res"]
    assert expected_error in result["errors"]


def test_generate_query_false_xml(xml_false_nit):
    """Test a incorrect generation and response of DTE
    by sending a false required information in the xml
    (NIT)
    """
    auth_headers = LoginHandler(
        user_sign="ASTECK",
        sign_key="cba1f67cb3ffc350489108c08f92fba3",
        user_api="ASTECK",
        api_key="7C7A187E9E8450B1F7812C7D6225A6AA",
    )
    result = generate_and_parse_query(
        auth_headers=auth_headers,
        identifier="123",
        xml=xml_false_nit,
    )
    expected_error = {
        "resultado": False,
        "fuente": "Firma Digital del Emisor",
        "categoria": "1",
        "numeral": "1",
        "validacion": "1",
        "mensaje_error": "Documento no firmado - FIRMA-XADES-BES-005,"
        + " Hubo un error, Por favor revise lo siguiente:"
        + " El numero de NIT asociado al certificado no concuerda con el NIT"
        + " del Emisor en el XML que intenta certificar. Secuencia: 15",
    }
    assert not result["res"]
    assert expected_error in result["errors"]


def test_both_apis(dte):
    """Test a correct generation and response of DTE
    by using gt_sat_api to create the xml
    """
    xml_from_api = dte_to_xml(dte)
    auth_headers = LoginHandler(
        user_sign="ASTECK",
        sign_key="cba1f67cb3ffc350489108c08f92fba3",
        user_api="ASTECK",
        api_key="7C7A187E9E8450B1F7812C7D6225A6AA",
    )
    result = generate_and_parse_query(
        auth_headers=auth_headers,
        identifier="123",
        xml=xml_from_api,
    )
    assert result["res"]
    assert result["xml"]
    assert result["date_certificate"]
    assert result["uuid"]
    assert result["series"]
    assert result["number"]
    assert ET.fromstring(result["xml"])
