from typing import Annotated
from fastapi import APIRouter, Form, HTTPException, Query, status

from models.Todo import Todo, Task

routes = APIRouter()

list_todos = [Todo(
   id=1,
   title='Initial App',
   tasks=[Task(
      title='Say hi!'
   )]
)]

@routes.get('', status_code=status.HTTP_200_OK)
def list_toDos():
   return list_todos

@routes.post('', status_code=status.HTTP_201_CREATED)
def create_todo(todo_name:Annotated[str, Form(), Query(min_length=3)]):
   todo_new = Todo(
      id=len(list_todos) + 1,
      title=todo_name
   )
   list_todos.append(todo_new)
   return todo_new

@routes.get("/{todo_id}", status_code=status.HTTP_200_OK)
def get_toDo(todo_id: int):
   todo_finded = [_todo for _todo in list_todos if _todo.id == todo_id]
   if len(todo_finded) == 0:
      raise HTTPException(status_code=404, detail="ToDo not found")
   
   return todo_finded[0]

@routes.put('/{id_todo}', status_code=status.HTTP_200_OK)
def update_toDo(id_todo:int, new_name:str):
   todo_finded = [_todo for _todo in list_todos if _todo.id == id_todo]
   if len(todo_finded) == 0:
      raise HTTPException(status_code=404, detail="ToDo not found")
   
   index = list_todos.index(todo_finded[0])
   update_Todo = Todo(
      id= todo_finded[0].id,
      title= new_name
   )

   list_todos[index] = update_Todo
   
   return update_Todo

@routes.post('/{id_todo}', status_code=201)
def add_task(id_todo:int, name_task:Annotated[str,Query(min_length=3)]):
   todo_finded = [_todo for _todo in list_todos if _todo.id == id_todo]
   if len(todo_finded) == 0:
      raise HTTPException(status_code=404, detail="ToDo not found")
   
   new_task = Task(
      title=name_task
   )
   todo_finded[0].tasks.append(new_task)
   return new_task
