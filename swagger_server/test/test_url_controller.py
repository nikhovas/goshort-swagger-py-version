# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.types_url import TypesUrl  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUrlController(BaseTestCase):
    """UrlController integration test stubs"""

    def test_delete_url(self):
        """Test case for delete_url

        Delete url by key
        """
        response = self.client.open(
            '/api//urls/{key}'.format(key='key_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_url(self):
        """Test case for get_url

        Get url by key
        """
        response = self.client.open(
            '/api//urls/{key}'.format(key='key_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_url(self):
        """Test case for patch_url

        Edit url by sent data
        """
        url = TypesUrl()
        response = self.client.open(
            '/api//urls/{key}'.format(key='key_example'),
            method='PATCH',
            data=json.dumps(url),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_url(self):
        """Test case for post_url

        Create url by sent data
        """
        url = TypesUrl()
        response = self.client.open(
            '/api//urls/',
            method='POST',
            data=json.dumps(url),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
