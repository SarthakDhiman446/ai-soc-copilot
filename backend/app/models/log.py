from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.database.database import Base


class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String(255), nullable=False)

    filepath = Column(String(500), nullable=False)

    file_size = Column(Integer, nullable=False)

    status = Column(
        String(50),
        default="uploaded"
    )

    uploaded_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )