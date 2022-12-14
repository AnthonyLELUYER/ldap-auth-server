# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.get_is_alive_response_isalive import GetIsAliveResponseIsalive
from openapi_server import util

from openapi_server.models.get_is_alive_response_isalive import GetIsAliveResponseIsalive  # noqa: E501

class GetIsAliveResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, isalive=None):  # noqa: E501
        """GetIsAliveResponse - a model defined in OpenAPI

        :param isalive: The isalive of this GetIsAliveResponse.  # noqa: E501
        :type isalive: List[GetIsAliveResponseIsalive]
        """
        self.openapi_types = {
            'isalive': List[GetIsAliveResponseIsalive]
        }

        self.attribute_map = {
            'isalive': 'isalive'
        }

        self._isalive = isalive

    @classmethod
    def from_dict(cls, dikt) -> 'GetIsAliveResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetIsAlive_response of this GetIsAliveResponse.  # noqa: E501
        :rtype: GetIsAliveResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def isalive(self):
        """Gets the isalive of this GetIsAliveResponse.


        :return: The isalive of this GetIsAliveResponse.
        :rtype: List[GetIsAliveResponseIsalive]
        """
        return self._isalive

    @isalive.setter
    def isalive(self, isalive):
        """Sets the isalive of this GetIsAliveResponse.


        :param isalive: The isalive of this GetIsAliveResponse.
        :type isalive: List[GetIsAliveResponseIsalive]
        """

        self._isalive = isalive
