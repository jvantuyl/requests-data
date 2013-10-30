import unittest
import requests
from requests_data.adapters import DataAdapter


class TestDataAdapter(unittest.TestCase):
    def test_data_get_text(self):
        """method GET -> 200 (text) for data-scheme"""
        s = requests.Session()
        s.mount('data:', DataAdapter())
        r = s.get('data:text/plain,This%20is%20a%20test.')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.content, 'This is a test.')
        self.assertEqual(r.text, u'This is a test.')

    def test_data_get_binary(self):
        """method GET -> 200 (binary) for data-scheme"""
        s = requests.Session()
        s.mount('data:', DataAdapter())
        r = s.get(
            'data:image/gif;base64,'
            'R0lGODlhAQABAHAAACH5BAUAAAAALAAAAAABAAEAAAICRAEAOw=='
        )
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.content,
            'GIF89a\x01\x00\x01\x00p\x00\x00!\xf9\x04\x05\x00\x00\x00'
            '\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;')

    def test_data_only_gets(self):
        """method DELETE -> 405 for data-scheme"""
        s = requests.Session()
        s.mount('data:', DataAdapter())
        r = s.delete('data:text/plain,GuineaPig')
        self.assertEqual(r.status_code, 405)
