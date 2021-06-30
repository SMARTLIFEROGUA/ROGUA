from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import List

from .emisor import Emisor
from .frase import Frase
from .item import Item
from .receptor import Receptor
from .total_impuesto import TotalImpuesto


@dataclass
class DTE:
    """Agrupa la estructura para un DTE."""

    clase_documento: str
    codigo_moneda: str
    fecha_hora_emision: datetime
    tipo: str
    emisor: Emisor
    receptor: Receptor
    frases: List[Frase]
    items: List[Item]
    totales_impuestos: List[TotalImpuesto]
    gran_total: Decimal
