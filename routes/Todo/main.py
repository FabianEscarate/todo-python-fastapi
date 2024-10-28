# from typing import Annotated
from fastapi import APIRouter, Form, HTTPException, Query, status, Depends

from models.Todo import Todo, Task, createTodo, createTask, TodoWithTasks
from core.todo import TodoController, Session, generate_session

routes = APIRouter()

@routes.get('', status_code=status.HTTP_200_OK, response_model=list[Todo])
def list_toDos():
   list_todos = TodoController().list_todos()
   return list_todos

@routes.post('', status_code=status.HTTP_201_CREATED, response_model=Todo)
def create_todo(new_todo: createTodo):   
   todo = Todo.model_validate(new_todo)
   toDo_result = TodoController().create_todo(todo)
   return toDo_result

@routes.get("/{todo_id}", status_code=status.HTTP_200_OK, response_model=TodoWithTasks)
def get_toDo(todo_id: int, session: Session = Depends(generate_session)):
   todo = session.get(Todo, todo_id)
   if not todo:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ToDo not found")
   return todo

@routes.put('/{id_todo}', status_code=status.HTTP_200_OK, response_model=Todo)
def update_toDo(id_todo: int, update_todo: createTodo):
   db_todo = TodoController().get_todo_by_id(id_todo)
   if not db_todo:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ToDo not found")
      
   updated_todo = TodoController().update_todo(db_todo, update_todo)
   return updated_todo

@routes.post('/{id_todo}', status_code=201, response_model=Task)
def add_task(id_todo:int, new_task: createTask):
   todo_controller = TodoController()
   todo = todo_controller.get_todo_by_id(id_todo)
   if todo == None:
      raise HTTPException(status_code=404, detail="ToDo not found")
   
   task_model = Task.model_validate(new_task, update={"todo_id": id_todo})
   task_added = todo_controller.add_task(task_model)
   return task_added
