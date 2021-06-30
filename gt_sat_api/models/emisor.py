from dataclasses import dataclass

from .direccion import Direccion


@dataclass
class Emisor:
    """Agrupa la información del Emisor del DTE."""

    afiliacion_iva: str
    codigo_establecimiento: int
    correo_emisor: str
    nit_emisor: str
    nombre_comercial: str
    nombre_emisor: str
    direccion: Direccion
