from fastapi import APIRouter
from api.v1.endpoints import todo


api_router = APIRouter()

api_router.include_router(todo.router, prefix="/todo", tags=["to-do"])