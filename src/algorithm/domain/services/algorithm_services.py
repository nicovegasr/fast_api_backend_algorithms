import os
import pandas as pd

from algorithm.domain.exceptions.algorithm_filenumber_invalid import FileNumberInvalid
from algorithm.domain.exceptions.algorithm_not_found import AlgorithmNotFound
from algorithm.domain.exceptions.algorithm_files_empty import FilesEmpty

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
    
    def validate(self, algorithm_dto):
        if len(algorithm_dto.files) == 0:
            raise FilesEmpty("The files of the algorithm are empty")
        for file in algorithm_dto.files:
            if file.file_number <= 0:
                raise FileNumberInvalid(str(file.name))            
        

    def algorithm_exists(self, algorithm_name):
        if self.algorithm_repository.algorithm_exists(algorithm_name):
            return True
        raise AlgorithmNotFound("Algorithm not found in server, check the folder models")
    
    def run_algorithm(self, algorithm_dto) -> list[pd.DataFrame]:
        pass
    
    def save_result(self, result):
        pass