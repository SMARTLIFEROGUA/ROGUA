""" Conection to FEEL """
import requests

from .login import LoginHandler

URL_FEEL = "https://certificador.feel.com.gt/fel/procesounificado/transaccion/v2/xml"


def send_query(auth: LoginHandler, identifier: str, xml: str) -> requests.Response:
    """Function that sends an xml to SAT trough FEEL API"""
    headers = {
        "UsuarioFirma": auth.user_sign,
        "LlaveFirma": auth.sign_key,
        "UsuarioApi": auth.user_api,
        "LlaveApi": auth.api_key,
        "Identificador": identifier,
    }
    request = requests.post(
        url=URL_FEEL,
        data=xml,
        headers=headers,
    )
    return request
