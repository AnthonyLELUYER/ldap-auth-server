from flask import abort
import jwt
import datetime
import core.mgt_logs.logging_api as lapi
import ldap
import os
from core.vault.Client import get_vault_secret
LOGGER = lapi.get_logger("generatetoken", "INFO")


def generate_token(payload):
    """
            Will try to match username and password in LDAP
            If there is a match, a JSON Web Token will be created and returned

    :param: Username and Password (JSON)
    :return: Return code and JWT (JSON)
    Return code is either 000 when it's failed, or 001 when it's succeeded
    """
    username = payload.get('username')
    ldap_user = "uid=%s,ou=Users,dc=company,dc=demo" % username
    password = payload.get('password')

    ldap_settings = get_vault_secret("prod/ldap")

    #secret_key = ldap_settings["secret_key"]
    secret_key = os.environ["SECRET"]

    # Check if user/password combination exists on LDAP server
    try:
        connect = ldap.initialize(ldap_settings["protocol"] + "://" + ldap_settings["URL"] + ":" + str(ldap_settings["port"]))
        connect.simple_bind_s(ldap_user, password)
    except ldap.INVALID_CREDENTIALS:
        abort(403, 'Username and password combination not recognized.')
    except ldap.LDAPError as e:
        LOGGER.error("ldap.LDAPERROR: " + str(e))
        abort(403, 'LDAP Error: ' + str(e))
    except Exception as err:
        abort(403, 'Exception: ' + str(err))

    try:
        # exp is the expiration date, iat is the time the token is generated, and sub is the subject
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=120),
            'iat': datetime.datetime.utcnow(),
            'sub': username
        }

        # That payload is then encoded with jwt module, which produce a byte object, which is then decoded to a String
        return {'cr': '001', 'result': jwt.encode(
            payload,
            secret_key,
            algorithm='HS256'
        )}

    except Exception as e:
        return {'cr': '000', 'result': str(e)}
