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
            algorithm_service.algorithm_exists(algorithm_dto.name)
            result = algorithm_service.run_algorithm(algorithm_dto)
            #algorithm_service.save_result(result)
        except FileNumberInvalid as e:
            raise HTTPException(status_code=401, detail="The file number of the file is invalid: " + str(e))
        except FilesEmpty as e:
            raise HTTPException(status_code=400, detail="Files of the algorithm are empty: " + str(e))
        except AlgorithmNotFound:
            raise HTTPException(status_code=404, detail="Algorithm not found in server, check the folder models")
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error running the algorithm: " + str(e)) 
        return {"message": "Algorithm runned successfully", result: result}
        
    
