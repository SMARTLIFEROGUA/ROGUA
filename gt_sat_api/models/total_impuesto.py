from dataclasses import dataclass
from decimal import Decimal


@dataclass
class TotalImpuesto:
    """Agrupa los datos de cada impuesto."""

    nombre_corto: str
    total_monto_impuesto: Decimal
