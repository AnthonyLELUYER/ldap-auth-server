import hvac
import os
from flask import abort
from core.mgt_conf.yaml_config import load_yaml_config


def get_vault_secret(path):
    """
    Instantiates a hvac / vault client, retrieve a secret in path, returns a JSON.
    :param path: string, Path to the secret(s), e.g. SmartOps/Secret
    :return: auth_sec: JSON, One or multiple key/value
    """

    cert_path = load_yaml_config()["etc"]["path"] + "../certificates/"
    service_name = "ldap-auth"

    if os.path.isfile(cert_path + service_name + ".crt"):
        # Certificates must be in that order (cert, key)
        certs = (cert_path + service_name + ".crt", cert_path + service_name + ".key")

        # Initiate a Vault Client
        vault_client = hvac.Client(
            url="https://vault.engine.company.com:8201",
            cert=certs
        )
        # Authentication
        vault_client.auth_tls()

        if vault_client.is_authenticated():
            # We read the secret on the "path" and mount_point "kv-v2"
            auth_sec = vault_client.secrets.kv.v2.read_secret_version(path=path, mount_point='kv-v2')
            return auth_sec["data"]["data"]
        else:
            abort(401, "Invalid certificates, vault connection failed.")
    else:
        abort(401, "Certificates don't exist.")
