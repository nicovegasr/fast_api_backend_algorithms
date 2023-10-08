import unittest

from fastapi.testclient import TestClient
from unittest.mock import patch

from api import app


class AlgorithmControllerGetTests(unittest.TestCase):
    def setUp(self):
        self.app = TestClient(app)

    def test_get_algorithms(self):
        # When
        with patch('algorithm.infraestructure.repositories.local_repository.AlgorithmLocalRepository.get_available_algorithms', return_value=["drivers", "zones"]):
            response = self.app.get("/api/v1/algorithms")
        # Then
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(response.json(), ["drivers", "zones"])

    def test_get_algorithms_empty(self):
        # When
        with patch('algorithm.infraestructure.repositories.local_repository.AlgorithmLocalRepository.get_available_algorithms', return_value=[]):
            response = self.app.get("/api/v1/algorithms")
        # Then
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.json(), {"detail": "Algorithms not found in server, check the folder models"})