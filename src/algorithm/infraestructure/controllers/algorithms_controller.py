from fastapi import APIRouter, HTTPException, status

from algorithm.domain.services.algorithm_services import AlgorithmServices
from algorithm.infraestructure.repositories.local_repository import AlgorithmLocalRepository

class AlgorithmController:
    def __init__(self):
        self.router = APIRouter()
        self.router.get("/api/v1/algorithms", status_code=status.HTTP_200_OK)(
            self.get_algorithms
        )
        self.router.post("/api/v1/run_algorithm", status_code=status.HTTP_200_OK)

    # TODO: Si quiero añadir una base de datos tengo que hacer las comprobaciones de que los algoritmos existan en la base de datos.
    # Hacer tipados propios de errores es hacer sobre ingeniería ya que FastAPI no facilita esta funcionalidad.
    async def get_algorithms(self):
        algorithm_repository = AlgorithmLocalRepository()
        algorithm_service = AlgorithmServices(algorithm_repository)
        algorithms = algorithm_service.get_algorithms()
        if not algorithms:
            raise HTTPException(status_code=404, detail="Algorithms not found in server, check the folder models")
        return algorithms
    
    async def run_algorithm(self):
        raise NotImplementedError
    
