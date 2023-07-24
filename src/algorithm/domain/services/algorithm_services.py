import os

from algorithm.domain.interfaces.algorithm_repository import AlgorithmRepository

class AlgorithmServices:
    def __init__(self, algorithm_repository: AlgorithmRepository):
        self.algorithm_repository = algorithm_repository
    
    # Funcion que devuelve los algoritmos disponibles en la carpeta models
    def get_algorithms(self):
      return self.algorithm_repository.get_available_algorithms()