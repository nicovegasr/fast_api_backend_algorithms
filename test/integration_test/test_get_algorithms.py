import unittest

from fastapi.testclient import TestClient

from api import app


class GetAlgorithmTests(unittest.TestCase):
    def setUp(self):
        self.app = TestClient(app)

    def test_get_algorithms(self):
        response = self.app.get("/get_algorithms")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), ["drivers"])

