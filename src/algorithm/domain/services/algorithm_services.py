import os

from algorithm.domain.interfaces.algorithm_repository import AlgorithmRepository

class AlgorithmServices:
    def __init__(self, algorithm_repository: AlgorithmRepository):
        self.algorithm_repository = algorithm_repository

    """
        * Get all the algorithms available in the server.
        * 
        * @return list[str] List of the names of the algorithms.
    """   
    def get_algorithms(self):
      return self.algorithm_repository.get_available_algorithms()