import unittest

from fastapi.testclient import TestClient

from api import app


class AlgorithmControllerTests(unittest.TestCase):
    def setUp(self):
        self.app = TestClient(app)

    def test_get_algorithms(self):
        response = self.app.get("/api/v1/algorithms")

        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(response.json(), ["drivers", "zones"])

    def test_run_algorithm(self):
        pass