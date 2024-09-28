from sqlmodel import SQLModel, Field, Relationship

class TodoBase(SQLModel):
   title: str

class Todo(TodoBase, table=True):
   id: int | None = Field(default=None, primary_key=True)
   tasks: list["Task"] = Relationship(back_populates="todo_group") 

class TodoWithTasks(TodoBase):
   id:int
   tasks: list["Task"] = []

class createTodo(TodoBase):
   pass

class TaskBase(SQLModel):
  title: str
  active: bool | None = Field(default=True)
  complete: bool | None = Field(default=False)
  todo_id:int | None  = Field(foreign_key="todo.id")
   
class Task(TaskBase, table=True):
  id: int | None = Field(default=None, primary_key=True)
  todo_group: Todo = Relationship(back_populates="tasks")

class taskPublic(TaskBase):
   id:int

class createTask(TaskBase):
   title: str
   todo_id: int | None = None
