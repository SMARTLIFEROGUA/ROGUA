from dataclasses import dataclass
from decimal import Decimal
from typing import List, Optional

from .impuesto import Impuesto


@dataclass
class Item:
    """Agrupa la información de un renglón o ítem de un DTE.

    Se refiere a lo que la Ley del IVA define como “concepto” en la venta de bienes o como
    “clase de servicio” en la prestación de servicios. También se refiere a lo que el
    Reglamento de la Ley del IVA indica como “detalle” o “descripción” de la venta, del
    servicio prestado o del arrendamiento."""

    bien_o_servicio: str
    numero_linea: int
    cantidad: Decimal
    descripcion: str
    precio_unitario: Decimal
    precio: Decimal
    impuestos: List[Impuesto]
    total: Decimal
    unidad_medida: Optional[str] = None
    descuento: Optional[Decimal] = None
