from sqlmodel import SQLModel, Field, Relationship

class Todo(SQLModel, table=True, arbitrary_types_allowed=True):
   id: int | None = Field(default=None, primary_key=True)
   title: str
   tasks: list["Task"] = Relationship(back_populates="todo_group") 

class Task(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  title: str
  active: bool = Field(default=True)
  complete: bool = Field(default=False)
  todo_id:int  = Field(foreign_key="todo.id")
  todo_group: Todo = Relationship(back_populates="tasks")

class createTodo(SQLModel):
   title:str
