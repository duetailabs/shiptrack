import unittest
import json
from unittest.mock import patch
from flask import Flask
from main import app  # Assuming your main code is in main.py
import time

class TestShippingService(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_discovery(self):
        """
        Test the /discovery endpoint.
        """
        response = self.app.get('/discovery')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['name'], "shipping")
        self.assertEqual(data['version'], "1.0")
        self.assertEqual(data['owners'], ["ameerabb", "lonestar"])
        self.assertEqual(data['team'], "genAIs")
        self.assertEqual(data['organization'], "acme")

    def test_liveness(self):
        """
        Test the /live endpoint.
        """
        response = self.app.get('/live')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data["status"], "live")
        self.assertEqual(data["code"], 200)
        self.assertIsNotNone(data["timestamp"])

    def test_readiness(self):
        """
        Test the /ready endpoint.
        """
        response = self.app.get('/ready')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data["status"], "ready")
        self.assertEqual(data["code"], 200)
        self.assertIsNotNone(data["timestamp"])

if __name__ == '__main__':
    unittest.main()
