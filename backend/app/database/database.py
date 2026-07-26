from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Temporary hardcoded credentials (NOT recommended for production)
DATABASE_USER = "postgres"
DATABASE_PASSWORD = "Sarthak@123"
DATABASE_HOST = "localhost"
DATABASE_PORT = "5432"
DATABASE_NAME = "ai_soc_copilot"

encoded_password = quote_plus(DATABASE_PASSWORD)

DATABASE_URL = (
    f"postgresql://{DATABASE_USER}:"
    f"{encoded_password}@"
    f"{DATABASE_HOST}:"
    f"{DATABASE_PORT}/"
    f"{DATABASE_NAME}"
)

engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()