from datetime import datetime

from pydantic import BaseModel


class LogResponse(BaseModel):
    id: int
    filename: str
    filepath: str
    file_size: int
    status: str
    uploaded_at: datetime

    class Config:
        from_attributes = True