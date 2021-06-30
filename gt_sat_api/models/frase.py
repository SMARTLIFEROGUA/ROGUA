from dataclasses import dataclass


@dataclass
class Frase:
    """En esta sección deberá indicarse los regímenes y textos especiales que son
    requeridos en los DTE,de acuerdo a la afiliación del contribuyente y tipo de operación."""

    codigo_escenario: int
    tipo_frase: int
