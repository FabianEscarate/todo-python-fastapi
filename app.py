from typing import Union, Annotated
from fastapi import FastAPI, HTTPException, Form, Query
from models.Todo import Todo, Task
from routes.main import route

class App():
  app = FastAPI()

  def start(self):
    self.app.include_router(route, prefix='/v1')
    return self.app