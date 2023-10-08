import unittest

from fastapi.testclient import TestClient
from unittest.mock import patch

from api import app


class AlgorithmControllerRunTests(unittest.TestCase):
    def setUp(self):
        self.app = TestClient(app)

    def test_run_non_existent_algorithm_should_return_not_found(self):
        response = self.app.post("/api/v1/run_algorithm", json={
            "name": "not_drivers",
            "files": [
                {
                    "file_number": 1,
                    "name": "drivers.csv",
                    "content": "id,name,age\n1,John,20\n2,Paul,30\n3,George,40\n4,Ringo,50"

                }
            ]
        })

        self.assertEqual(response.status_code, 404)

    def test_run_algorithm_without_files_should_return_bad_request(self):
        response = self.app.post("/api/v1/run_algorithm", json={
            "name": "drivers",
            "files": []
        })
        self.assertEqual(response.status_code, 400)

    def test_run_algorithm_with_negative_file_number(self):
        response = self.app.post("/api/v1/run_algorithm", json={
            "name": "drivers",
            "files": [
                {
                    "name": "drivers.csv",
                    "file_number": -1,
                    "content": "id,name,age\n1,John,20\n2,Paul,30\n3,George,40\n4,Ringo,50"
                }
            ]
        })
        self.assertEqual(response.status_code, 401)
