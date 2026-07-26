print("Step 1")

from sqlalchemy import Column, Integer, String, DateTime

print("Step 2")

from sqlalchemy.sql import func

print("Step 3")

from app.database.database import Base

print("Step 4")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(20), default="analyst")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

print("Step 5")