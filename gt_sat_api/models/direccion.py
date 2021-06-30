from dataclasses import dataclass


@dataclass
class Direccion:
    """Agrupa los datos de la dirección"""

    direccion: str
    codigo_postal: str
    municipio: str
    departamento: str
    pais: str
