from fastapi import APIRouter, HTTPException, status
from algorithm.domain.exceptions.algorithm_filenumber_invalid import FileNumberInvalid

from algorithm.domain.services.algorithm_services import AlgorithmServices
from algorithm.domain.exceptions.algorithm_not_found import AlgorithmNotFound
from algorithm.domain.exceptions.algorithm_files_empty import FilesEmpty

from algorithm.infraestructure.repositories.local_repository import AlgorithmLocalRepository
from algorithm.infraestructure.dtos.algorithm_dto import AlgorithmDTO

class AlgorithmController:
    """
        * Constructor of the algorithm controller where the routes are defined.
        * @param AlgorithmLocalRepository algorithm_repositor 
    """
    def __init__(self):
        self.router = APIRouter()
        self.router.get("/api/v1/algorithms", status_code=status.HTTP_200_OK)(
            self.get_algorithms
        )
        self.router.post("/api/v1/run_algorithm", status_code=status.HTTP_200_OK)(
            self.run_algorithm
        )
    
    """
        * Get all the algorithms available in the server with the service and if there is no algorithms, raise an exception.
    """
    async def get_algorithms(self):
        algorithm_repository = AlgorithmLocalRepository()
        algorithm_service = AlgorithmServices(algorithm_repository)
        algorithms = algorithm_service.get_algorithms()
        if not algorithms:
            raise HTTPException(status_code=404, detail="Algorithms not found in server, check the folder models")
        return algorithms
    
    async def run_algorithm(self, algorithm_dto: AlgorithmDTO):
        algorithm_repository = AlgorithmLocalRepository()
        algorithm_service = AlgorithmServices(algorithm_repository)
        try:
            algorithm_service.validate(algorithm_dto)
            result = algorithm_service.run_algorithm(algorithm_dto)
        except FileNumberInvalid as message_error:
            raise HTTPException(status_code=401, detail=f"{str(message_error)}")
        except FilesEmpty as message_error:
            raise HTTPException(status_code=400, detail=f"{str(message_error)}")
        except AlgorithmNotFound as message_error:
            raise HTTPException(status_code=404, detail=f"{str(message_error)}")
        except Exception as message_error:
            raise HTTPException(status_code=500, detail="Error running the algorithm: " + str(message_error)) 
        return {"message": "Algorithm runned successfully", result: result}
        
    
