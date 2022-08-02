# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.classify_ticket import ClassifyTicket  # noqa: E501
from openapi_server.models.classify_ticket_response import ClassifyTicketResponse  # noqa: E501
from openapi_server.models.filter_ticket import FilterTicket  # noqa: E501
from openapi_server.models.filter_ticket_response import FilterTicketResponse  # noqa: E501
from openapi_server.models.get_metric_response import GetMetricResponse  # noqa: E501
from openapi_server.models.get_ticket_response import GetTicketResponse  # noqa: E501
from openapi_server.models.update_ticket import UpdateTicket  # noqa: E501
from openapi_server.models.update_ticket_response import UpdateTicketResponse  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_classify_ticket_post(self):
        """Test case for classify_ticket_post

        
        """
        classify_ticket = {
  "path" : "/var/www",
  "server" : "server1",
  "host" : "host1",
  "description" : "issue in",
  "servity" : "WARNING",
  "ticket_id" : "id_0001"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/classifyTicket',
            method='POST',
            headers=headers,
            data=json.dumps(classify_ticket),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_filter_ticket_post(self):
        """Test case for filter_ticket_post

        
        """
        filter_ticket = {
  "filter" : "issue in",
  "ticket_id" : "id_0001"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/filterTicket',
            method='POST',
            headers=headers,
            data=json.dumps(filter_ticket),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_metric_get(self):
        """Test case for get_metric_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/getMetric',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ticket_get(self):
        """Test case for get_ticket_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/getTicket',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_ticket_post(self):
        """Test case for update_ticket_post

        
        """
        update_ticket = {
  "ticket_id" : "id_0001",
  "updateTicket" : "issue in"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/updateTicket',
            method='POST',
            headers=headers,
            data=json.dumps(update_ticket),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
