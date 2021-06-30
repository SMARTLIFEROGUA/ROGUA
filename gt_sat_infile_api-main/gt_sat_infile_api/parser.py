""" Main functionality """
import base64
import json
from typing import Any, Dict

from .conection import send_query
from .login import LoginHandler


def parse_certificated_xml(encoded_xml: str) -> str:
    """ Parse certificated xml into a legible string """
    xml = base64.b64decode(encoded_xml)
    return xml.decode()


def generate_and_parse_query(
    auth_headers: LoginHandler,
    identifier: str,
    xml: str,
) -> dict:
    """Request and process a certificated xml"""
    do_request = send_query(auth_headers, identifier, xml)
    request_info = json.loads(do_request.text)
    result: Dict[str, Any] = {}
    if request_info["resultado"]:
        result["res"] = True
        result["xml"] = parse_certificated_xml(request_info["xml_certificado"])
        result["date_certificate"] = request_info["fecha"]
        result["uuid"] = request_info["uuid"]
        result["series"] = request_info["serie"]
        result["number"] = request_info["numero"]
    else:
        result["res"] = False
        result["errors"] = request_info["descripcion_errores"]

    return result
