import unittest

from algorithm.domain.services.algorithm_services import AlgorithmServices
from algorithm.infraestructure.repositories.local_repository import AlgorithmLocalRepository

class AlgorithmServicesGetTests(unittest.TestCase):
    def test_get_algorithms_should_return_at_least_one_algorithm(self):
        algorithm_repository =  AlgorithmLocalRepository()
        algorithm_services = AlgorithmServices(algorithm_repository)
        algorithms = algorithm_services.get_algorithms()
        
        self.assertGreater(len(algorithms), 0)

    # def test_run_algorithm(self):
    #     algorithm_services = AlgorithmServices(algorithm_repository=None)
        
    #     algorithm_services.run_algorithm()
        
    #     self.assertTrue(True)