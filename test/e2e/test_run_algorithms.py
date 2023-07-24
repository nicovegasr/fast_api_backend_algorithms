import unittest

from fastapi.testclient import TestClient
from unittest.mock import patch

from api import app


class AlgorithmControllerRunTests(unittest.TestCase):
    def setUp(self):
        self.app = TestClient(app)

    def test_run_algorithm(self):
        response = self.app.post("/api/v1/run_algorithm", json={
            "name": "drivers",
            "files": [
                {
                    "file_number": 1,
                    "name": "drivers.csv",
                    "content": "id,name,age\n1,John,20\n2,Paul,30\n3,George,40\n4,Ringo,50"

                }
            ]
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Algorithm runned successfully"})