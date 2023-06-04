import unittest

from algorithm.domain.services.algoritm_services import AlgorithmServices


class AlgorithmServicesTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_algorithms(self):
        algorithm_services = AlgorithmServices(algorithm_repository=None)
        algorithms = algorithm_services.get_algorithms()
        self.assertEqual(algorithms, ["drivers", "zones"])
