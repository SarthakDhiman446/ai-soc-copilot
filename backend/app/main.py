from fastapi import FastAPI
from app.api.v1.logs import router as logs_router
from app.api.v1.auth import router as auth_router

app = FastAPI(
    title="AI SOC Copilot",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(logs_router)