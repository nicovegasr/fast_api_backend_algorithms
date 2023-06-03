from fastapi import FastAPI

from algorithm.infraestructure.controllers.algorithms_controller import AlgorithmController

app = FastAPI()
app.include_router(AlgorithmController().router)
