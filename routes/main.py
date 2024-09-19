from fastapi import APIRouter
from routes.Todo.main import routes

route = APIRouter()

route.include_router(routes, prefix='/todo', tags=['to-do'])
