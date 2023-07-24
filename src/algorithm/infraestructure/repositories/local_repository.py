import os
import pandas as pd

from algorithm.domain.interfaces.algorithm_repository import AlgorithmRepository

class AlgorithmLocalRepository(AlgorithmRepository):
    def __init__(self):
        pass

    def get_available_algorithms(self) -> list[str]:
      models_path =  os.path.dirname(os.path.realpath(__file__)).rsplit("infraestructure", 1)[0] + "domain/models/"
      algorithms =  [name for name in os.listdir(models_path) if os.path.isdir(os.path.join(models_path, name))]
      return algorithms

    def save_last_result(self, algorithm_result: list[pd.DataFrame]) -> None:
        pass

    def get_last_result(self) -> str:
        pass
    