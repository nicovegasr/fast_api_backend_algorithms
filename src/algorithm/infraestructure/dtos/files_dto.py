from fastapi import BaseModel

class FileDTO(BaseModel):
  name: str
  content: str