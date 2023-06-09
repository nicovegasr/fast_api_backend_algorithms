import os

from algorithm.domain.interfaces.algorithm_repository import AlgorithmRepository


class AlgorithmServices:
    def __init__(self, algorithm_repository: AlgorithmRepository):
        self.algorithm_repository = algorithm_repository
    
    # Funcion que devuelve los algoritmos disponibles en la carpeta models
    def get_algorithms(self):
      return os.listdir(os.path.dirname(os.path.realpath(__file__)).rsplit("services", 1)[0] + "/models/")
    