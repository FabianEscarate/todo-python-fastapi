# from pydantic import BaseModel
from models.Todo import Todo
from services.database import generate_session, Session


class TodoController():
  session: Session | None = None

  def __init__(self) -> "TodoController":
    self.session = generate_session()

  def create_todo(self, new_todo):
    self.session.add(new_todo)
    self.session.commit()
    self.session.refresh(new_todo)
    return new_todo
    
  