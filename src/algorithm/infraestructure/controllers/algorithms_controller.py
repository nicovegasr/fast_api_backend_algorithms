from fastapi import APIRouter, status


class AlgorithmController:
    def __init__(self):
        self.router = APIRouter()
        self.router.get("/get_algorithms", status_code=status.HTTP_200_OK)(
            self.get_algorithms
        )

    def get_algorithms(self):
        return ["drivers"]
