from fastapi import APIRouter, status

from algorithm.domain.services.algoritm_services import AlgorithmServices


class AlgorithmController:
    def __init__(self):
        self.router = APIRouter()
        self.router.get("/get_algorithms", status_code=status.HTTP_200_OK)(
            self.get_algorithms
        )

    async def get_algorithms(self):
        algorithm_service = AlgorithmServices(None)
        return algorithm_service.get_algorithms()
    
    
