from pydantic import BaseModel


class FileDTO(BaseModel):
    file_number: int
    name: str
    content: str
