from config.setting import settings
from sqlmodel import create_engine, SQLModel, Session, select, col
import models.Todo

engine = create_engine(settings.get("url_database"), echo=True)

def generate_session():
  with Session(engine) as session:
    yield session

def create_database():
  SQLModel.metadata.create_all(engine)
