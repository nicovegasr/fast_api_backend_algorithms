import unittest

from algorithm.domain.services.algorithm_services import AlgorithmServices


class AlgorithmServicesGetTests(unittest.TestCase):
    def test_get_algorithms(self):
        algorithm_services = AlgorithmServices(algorithm_repository=None)
        
        algorithms = algorithm_services.get_algorithms()
        
        self.assertCountEqual(algorithms, ["drivers", "zones"])