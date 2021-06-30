from dataclasses import dataclass
from typing import Optional

from .direccion import Direccion


@dataclass
class Receptor:
    """Agrupa la información del Receptor."""

    correo_receptor: str
    id_receptor: str
    nombre_receptor: str
    direccion: Optional[Direccion] = None
