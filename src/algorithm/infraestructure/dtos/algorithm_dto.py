from pydantic import BaseModel

from algorithm.infraestructure.dtos.files_dto import FileDTO


class AlgorithmDTO(BaseModel):
    name: str
    files: list[FileDTO]
