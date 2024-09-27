from typing import Annotated
from fastapi import APIRouter, Form, HTTPException, Query, status, Depends

from models.Todo import Todo, Task, createTodo, createTask, TodoWithTasks
from core.todo import TodoController, Session, generate_session

routes = APIRouter()

# list_todos = [Todo(
#    id=1,
#    title='Initial App',
#    tasks=[Task(
#       title='Say hi!'
#    )]
# )]


@routes.get('', status_code=status.HTTP_200_OK)
def list_toDos():
   list_todos = TodoController().list_todos()
   return list_todos

@routes.post('', status_code=status.HTTP_201_CREATED)
def create_todo(new_todo: createTodo):   
   todo = Todo.model_validate(new_todo)
   toDo_result = TodoController().create_todo(todo)
   return toDo_result

@routes.get("/{todo_id}", response_model=TodoWithTasks, status_code=status.HTTP_200_OK)
def get_toDo(todo_id: int, session: Session = Depends(generate_session)):
   todo = session.get(Todo, todo_id)
   if not todo:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ToDo not found")
   return todo


# @routes.put('/{id_todo}', status_code=status.HTTP_200_OK)
# def update_toDo(id_todo:int, new_name:str):
#    todo_finded = [_todo for _todo in list_todos if _todo.id == id_todo]
#    if len(todo_finded) == 0:
#       raise HTTPException(status_code=404, detail="ToDo not found")
   
#    index = list_todos.index(todo_finded[0])
#    update_Todo = Todo(
#       id= todo_finded[0].id,
#       title= new_name
#    )

#    list_todos[index] = update_Todo
   
#    return update_Todo

@routes.post('/{id_todo}', status_code=201)
def add_task(id_todo:int, new_task: createTask):
   todo_controller = TodoController()
   todo = todo_controller.get_todo_by_id(id_todo)
   if todo == None:
      raise HTTPException(status_code=404, detail="ToDo not found")
   
   task_model = Task.model_validate(new_task, update={"todo_id": id_todo})
   task_added = todo_controller.add_task(task_model)
   return new_task
