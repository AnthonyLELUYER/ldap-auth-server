# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class LDAPAuth(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, password=None, username=None):  # noqa: E501
        """LDAPAuth - a model defined in OpenAPI

        :param password: The password of this LDAPAuth.  # noqa: E501
        :type password: str
        :param username: The username of this LDAPAuth.  # noqa: E501
        :type username: str
        """
        self.openapi_types = {
            'password': str,
            'username': str
        }

        self.attribute_map = {
            'password': 'password',
            'username': 'username'
        }

        self._password = password
        self._username = username

    @classmethod
    def from_dict(cls, dikt) -> 'LDAPAuth':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LDAPAuth of this LDAPAuth.  # noqa: E501
        :rtype: LDAPAuth
        """
        return util.deserialize_model(dikt, cls)

    @property
    def password(self):
        """Gets the password of this LDAPAuth.


        :return: The password of this LDAPAuth.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this LDAPAuth.


        :param password: The password of this LDAPAuth.
        :type password: str
        """

        self._password = password

    @property
    def username(self):
        """Gets the username of this LDAPAuth.


        :return: The username of this LDAPAuth.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this LDAPAuth.


        :param username: The username of this LDAPAuth.
        :type username: str
        """

        self._username = username
