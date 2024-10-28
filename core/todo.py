# from pydantic import BaseModel
from models.Todo import Todo, Task, createTodo, createTask, TodoWithTasks
from services.database import generate_session, Session, select


class TodoController():
  # session: Session | None = None

  def __init__(self) -> "TodoController":
    self.session = generate_session().__next__()
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
    
  def update_todo(self, current_todo: Todo, updated_todo: Todo):
    with self.session as sess:
      db_todo = sess.get(self.model, current_todo.id)
      update_todo = updated_todo.model_dump(exclude_unset=True)
      db_todo.sqlmodel_update(update_todo)
      sess.add(db_todo)
      sess.commit()
      sess.refresh(db_todo)
      return db_todo
    
  def get_todo_by_id(self, todo_id: int):
    with self.session as sess:
      db_todo = sess.get(self.model, todo_id)
      return self.model.model_validate(db_todo)
    
  def get_todo_with_tasks_by_id(self, todo_id:int):
    with self.session as sess:
      db_todo = sess.get(self.model, todo_id)
      tasks = sess.exec(select(Task).where(Task.todo_id == db_todo.id)).all()
      db_todo.tasks = tasks
      return TodoWithTasks.model_validate(db_todo)
    
  def add_task(self,new_task: createTask):
    with self.session as sess:
      sess.add(new_task)
      sess.commit()
      sess.refresh(new_task)
      return new_task
  