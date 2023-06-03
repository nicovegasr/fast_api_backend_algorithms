from fastapi import BaseModel
from .files_dto import FileDTO

class AlgorithmDTO(BaseModel):
  name: str
  files: list[FileDTO]


