""" Test configurations """
from datetime import datetime
from importlib import resources

import pytest
from gt_sat_api import DTE, Direccion, Emisor, Frase, Impuesto, Item, Receptor, TotalImpuesto

from . import examples


@pytest.fixture
def dte():
    """Creates basic DTE"""
    emisor = Emisor(
        afiliacion_iva="GEN",
        codigo_establecimiento=1,
        correo_emisor="demo@demo.com.gt",
        nit_emisor="9847847",
        nombre_comercial="DEMO",
        nombre_emisor="DEMO, SOCIEDAD ANONIMA",
        direccion=Direccion(
            direccion="CUIDAD",
            codigo_postal="01001",
            municipio="GUATEMALA",
            departamento="GUATEMALA",
            pais="GT",
        ),
    )
    receptor = Receptor(
        correo_receptor="leyoalvizures4456@gmail.com",
        id_receptor="76365204",
        nombre_receptor="Jaime Alvizures",
        direccion=Direccion(
            direccion="CUIDAD",
            codigo_postal="01001",
            municipio="GUATEMALA",
            departamento="GUATEMALA",
            pais="GT",
        ),
    )
    items = [
        Item(
            bien_o_servicio="B",
            numero_linea="1",
            cantidad=1.00,
            unidad_medida="UND",
            descripcion="PRODUCTO1",
            precio_unitario=120.00,
            precio=120.00,
            descuento=0.00,
            impuestos=[
                Impuesto(
                    nombre_corto="IVA",
                    codigo_unidad_gravable=1,
                    monto_gravable=107.14,
                    monto_impuesto=12.86,
                ),
            ],
            total=120.00,
        ),
    ]
    new_dte = DTE(
        clase_documento="dte",
        codigo_moneda="GTQ",
        fecha_hora_emision=datetime.fromisoformat("2020-04-21T09:58:00-06:00"),
        tipo="FACT",
        emisor=emisor,
        receptor=receptor,
        frases=[
            Frase(codigo_escenario=1, tipo_frase=1),
            Frase(codigo_escenario=1, tipo_frase=2),
        ],
        items=items,
        totales_impuestos=[
            TotalImpuesto(nombre_corto="IVA", total_monto_impuesto=12.86),
        ],
        gran_total=120.00,
    )
    return new_dte


@pytest.fixture
def xml_example():
    """Get XML content of examples/Factura.xml"""
    example = resources.read_text(examples, "Factura.xml")
    return example


@pytest.fixture
def xml_false_nit():
    """Get XML content of examples/Factura_nit_falso.xml"""
    example = resources.read_text(examples, "Factura_nit_falso.xml")
    return example
