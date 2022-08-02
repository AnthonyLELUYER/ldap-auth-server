import jwt
import os
from core.vault.Client import get_vault_secret
import core.mgt_logs.logging_api as lapi
LOGGER = lapi.get_logger("tokenauthserver", "INFO")


def decode_auth_token(auth_token):
    """
            Decodes the auth token

    :param: auth_token
    :return: Return code and Message (json)
    Return code is either 000 when it's failed, or 001 when it's succeeded
    """
    #ldap_settings = get_vault_secret("prod/ldap")
    #secret_key = ldap_settings["secret_key"]
    
    secret_key = os.environ["SECRET"]

    try:
        payload = jwt.decode(auth_token, secret_key, algorithms='HS256')
        LOGGER.debug("Token: " + auth_token + " OK.")
        return {'cr': '001', 'result': 'Token OK', 'username': payload["sub"]}
    except jwt.ExpiredSignatureError:
        LOGGER.error("Token: " + auth_token + "KO. Signature expired. Please log in again.")
        return {'cr': '000', 'result': 'Signature expired. Please log in again.'}
    except jwt.InvalidTokenError:
        LOGGER.error("Token: " + auth_token + "KO. Invalid token. Please log in again.")
        return {'cr': '000', 'result': 'Invalid token. Please log in again.'}
