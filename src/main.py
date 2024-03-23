from fastapi import FastAPI, Request
from schemas.healthcheck import HealthCheck
from api.v1.api_v1 import api_router

app = FastAPI(title="TO-DO")

@app.get("/", response_model=HealthCheck, tags=["HealthCheck"])
async def health_check(request: Request):
    return {"message": "OK"}

app.include_router(api_router, prefix="/api/v1")