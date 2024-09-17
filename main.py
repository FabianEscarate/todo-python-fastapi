from typing import Union, Annotated
from fastapi import FastAPI, HTTPException, Form, Query

from models.Todo import Todo, Task

app = FastAPI()

list_todos = [Todo(
   id=1,
   title='Initial App',
   tasks=[Task(
      title='Say hi!'
   )]
)]

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/todo")
def todos():
   """
   some DOcumentation
   """
   return list_todos

@app.post('/todo', status_code=201)
def create_todo(todo_name:Annotated[str, Form(), Query(min_length=3)]):
   todo_new = Todo(
      id=len(list_todos) + 1,
      title=todo_name
   )
   list_todos.append(todo_new)
   return todo_new

@app.get("/todo/{todo_id}")
def todo(todo_id: int):
   todo_finded = [_todo for _todo in list_todos if _todo.id == todo_id]
   if len(todo_finded) == 0:
      raise HTTPException(status_code=404, detail="Todo not found")
   
   return todo_finded[0]

@app.post('/todo/{id_todo}', status_code=201)
def add_task(id_todo:int, name_task:Annotated[str,Query(min_length=3)]):
   todo_finded = [_todo for _todo in list_todos if _todo.id == id_todo]
   if len(todo_finded) == 0:
      raise HTTPException(status_code=404, detail="Todo not found")
   
   new_task = Task(
      title=name_task
   )
   todo_finded[0].tasks.append(new_task)
   return new_task

