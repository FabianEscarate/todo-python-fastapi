# from pydantic import BaseModel
from models.Todo import Todo, Task, createTodo, createTask
from services.database import generate_session, Session, select


class TodoController():
  # session: Session | None = None

  def __init__(self) -> "TodoController":
    self.session = generate_session()
    self.model = Todo

  def list_todos(self):
    with self.session as sess:
      statement = select(self.model)
      result = sess.exec(statement)
      return result.all()

  def create_todo(self, new_todo: createTodo):
    with self.session as sess:
      sess.add(new_todo)
      sess.commit()
      sess.refresh(new_todo)
      return new_todo
    
  def get_todo_by_id(self,todo_id: int):
    with self.session.__next__() as sess:
      result = sess.get(self.model, todo_id)
      print(result)
      yield result
    
  def add_task(self,new_task: createTask):
    with self.session as sess:
      sess.add(new_task)
      sess.commit()
      sess.refresh(new_task)
      return new_task
  