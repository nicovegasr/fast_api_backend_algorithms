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
        * @return list[str] List of algorithm's name.
    """   
    def get_algorithms(self):
      return self.algorithm_repository.get_available_algorithms()
    

    
    def run_algorithm(self, algorithm_dto) -> list[pd.DataFrame]:
        pass
    
    def validate(self, algorithm_dto):
        if len(algorithm_dto.files) == 0:
            raise FilesEmpty()
        for file in algorithm_dto.files:
            if file.file_number <= 0:
                raise FileNumberInvalid(file.name)            
        if not self.algorithm_repository.algorithm_exists(algorithm_dto.name):
            raise AlgorithmNotFound()