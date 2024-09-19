from typing import Union, Annotated
from fastapi import FastAPI, HTTPException, Form, Query

from models.Todo import Todo, Task
from routes.main import route

app = FastAPI()

app.include_router(route, prefix='/v1')

