import unittest
from unittest.mock import MagicMock

from algorithm.domain.exceptions.algorithm_filenumber_invalid import FileNumberInvalid
from algorithm.domain.exceptions.algorithm_files_empty import FilesEmpty
from algorithm.domain.services.algorithm_services import AlgorithmServices
from algorithm.infraestructure.repositories.local_repository import AlgorithmLocalRepository

class AlgorithmServicesGetTests(unittest.TestCase):
    algorithm_repository =  AlgorithmLocalRepository()
    algorithm_services = AlgorithmServices(algorithm_repository)

    def test_get_algorithms_should_return_at_least_one_algorithm(self):
        # When
        self.algorithm_repository.get_available_algorithms = MagicMock(return_value=["Drivers"])
        algorithms = self.algorithm_services.get_algorithms()
        # Then
        self.assertGreater(len(algorithms), 0)

    def test_validate_algorithm_data_should_return_files_empty(self):
        # When
        algorithm_dto = MagicMock()
        algorithm_dto.files = []
        with self.assertRaises(Exception) as context:
            AlgorithmServices.validate(algorithm_dto)
        # Then
        self.assertIsInstance(context.exception, FilesEmpty)
        self.assertTrue("The files of the algorithm are empty" in str(context.exception))

    def test_validate_algorithm_data_should_return_file_number_invalid(self):
        files = MagicMock()
        files.name = "test"
        files.file_number = -1
        algorithm_dto = MagicMock()
        algorithm_dto.files = [files]
        with self.assertRaises(Exception) as context:
            AlgorithmServices.validate(algorithm_dto)
        # Then
        self.assertIsInstance(context.exception, FileNumberInvalid)
        self.assertEqual("The file number of the file: test is invalid", str(context.exception))