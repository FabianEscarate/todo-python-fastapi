from pydantic import BaseModel

class Task(BaseModel):
  title: str
  active: bool = True
  complete: bool = False

class Todo(BaseModel):
   id: int
   title: str
   tasks: list[Task] = []
