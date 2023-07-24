import unittest

from algorithm.domain.services.algorithm_services import AlgorithmServices
from algorithm.infraestructure.repositories.local_repository import AlgorithmLocalRepository

class AlgorithmServicesGetTests(unittest.TestCase):
    def test_get_algorithms(self):
        algorithm_repository =  AlgorithmLocalRepository()
        algorithm_services = AlgorithmServices(algorithm_repository)
        algorithms = algorithm_services.get_algorithms()
        
        self.assertCountEqual(algorithms, ["drivers", "zones"])

    # def test_run_algorithm(self):
    #     algorithm_services = AlgorithmServices(algorithm_repository=None)
        
    #     algorithm_services.run_algorithm()
        
    #     self.assertTrue(True)