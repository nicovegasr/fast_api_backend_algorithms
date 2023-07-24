from abc import abstractmethod, ABCMeta
import pandas as pd

class AlgorithmRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_available_algorithms(self) -> list[str]:
        raise NotImplementedError

    @abstractmethod
    def save_last_result(self, algorithm_result: list[pd.DataFrame]) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_last_result(self) -> str:
        raise NotImplementedError
