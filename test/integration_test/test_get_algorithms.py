import unittest

from api import app

class GetAlgorithmTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_get_algorithms(self):
        response = self.app.get("/get_algorithms")
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.data), 0)