import connexion
from flask import make_response, abort
from werkzeug.exceptions import BadRequest
from openapi_server.models.get_is_alive_response import GetIsAliveResponse  # noqa: E501
from openapi_server.models.get_is_alive_response_isalive import GetIsAliveResponseIsalive
from openapi_server.models.ldap_auth import LDAPAuth  # noqa: E501
from openapi_server.models.ldap_auth_response import LdapAuthResponse  # noqa: E501
from openapi_server.models.verify_token import VerifyToken  # noqa: E501
from openapi_server.models.verify_token_response import VerifyTokenResponse  # noqa: E501
import core.auth.GenerateToken as cagt
import core.auth.VerifyToken as cavt
import core.mgt_logs.logging_api as lapi

LOGGER = lapi.get_logger("ldapauthserver", "DEBUG")


def get_isalive():  # noqa: E501
    """get_isalive

     # noqa: E501


    :rtype: getisaliveresponse
    """

    uri1 = "/isalive"
    title1 = "IsAlive"
    description1 = "The REST API is on air for gitinterface-openapi-server API"
    getisaliveresponseisalive1 = GetIsAliveResponseIsalive(uri=uri1, title=title1, description=description1)

    uri2 = "/isalive"
    title2 = "IsAlive"
    description2 = "The REST API is on air for gitinterface-openapi-server API"
    getisaliveresponseisalive2 = GetIsAliveResponseIsalive(uri=uri2, title=title2, description=description2)

    getisaliveresponse = GetIsAliveResponse([getisaliveresponseisalive1, getisaliveresponseisalive2])

    return getisaliveresponse


def ldapauth_post(ldap_auth=None):  # noqa: E501
    """ldapauth_post

     # noqa: E501

    :param ldap_auth: 
    :type ldap_auth: dict | bytes

    :rtype: LdapAuthResponse
    """
    if connexion.request.is_json:
        ldap_auth = LDAPAuth.from_dict(connexion.request.get_json())  # noqa: E501
        LOGGER.info("Payload content: " + str(ldap_auth))
        ldap_auth = ldap_auth.to_dict()

        if len(ldap_auth) == 0:
            abort(406, "no data into http POST")
        else:
            # convert post data receives
            #             each parameter is in res table access by the name declared into init...
            # do the job from a core class external to restserver of course...
            results = cagt.generate_token(ldap_auth)
            LOGGER.info(results)
            if results is not None and len(results) > 0:
                return make_response(results)
            else:
                return BadRequest("Bad Return from xxxx")


def verifytoken_post(verify_token=None):  # noqa: E501
    """verifytoken_post

     # noqa: E501

    :param verify_token: 
    :type verify_token: dict | bytes

    :rtype: VerifyTokenResponse
    """
    if connexion.request.is_json:
        verify_token = VerifyToken.from_dict(connexion.request.get_json())  # noqa: E501
        LOGGER.info("Payload content: " + str(verify_token))
        verify_token = verify_token.to_dict()

        if len(verify_token) == 0:
            abort(401, "no data into http POST")
        else:
            # convert post data receives
            #             each parameter is in res table access by the name declared into init...
            # do the job from a core class external to restserver of course...
            results = cavt.decode_auth_token(verify_token["auth_token"])
            LOGGER.info(results)
            if results is not None and len(results) > 0:
                return make_response(results)
            else:
                return BadRequest("Bad Return from xxxx")
