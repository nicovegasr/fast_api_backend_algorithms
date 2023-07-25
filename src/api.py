#import uvicorn

from fastapi import FastAPI

from algorithm.infraestructure.controllers.algorithms_controller import AlgorithmController

app = FastAPI()
app.include_router(AlgorithmController().router)

#uvicorn.run(app, host="0.0.0.0", port=8000)
