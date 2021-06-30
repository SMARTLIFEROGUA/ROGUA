from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass
class Impuesto:
    """Agrupa los datos de un Impuesto."""

    nombre_corto: str
    codigo_unidad_gravable: int
    monto_impuesto: Decimal
    monto_gravable: Optional[Decimal] = None
    cantidad_unidades_gravables: Optional[Decimal] = None
