from decimal import Decimal
from importlib import resources

import jinja2

from .. import templates
from ..models.dte import DTE


def dte_to_xml(dte: DTE) -> str:
    """Parse DTE python object to XML"""
    factura_template = resources.read_text(templates, "Factura.xml.jinja")
    jinja_template = jinja2.Template(factura_template, trim_blocks=True, lstrip_blocks=True)
    total_dte = compute_dte_totals(dte)
    xml_rendered = jinja_template.render(dte=dte, total=total_dte) + "\n"
    return xml_rendered


def compute_dte_totals(dte: DTE) -> Decimal:
    """Compute the document total values"""
    total = Decimal(0)
    for item in dte.items:
        total += Decimal(item.precio)
    return total
