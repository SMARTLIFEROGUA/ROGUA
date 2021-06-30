""" Login Handler """
from dataclasses import dataclass


@dataclass
class LoginHandler:
    """ Login Class """

    user_sign: str
    sign_key: str
    user_api: str
    api_key: str
