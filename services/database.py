from config.setting import settings
from sqlmodel import create_engine, SQLModel, Session
import models.Todo

engine = create_engine(settings.get("url_database"), echo=True)

def generate_session():
  session = Session(engine)
  return session

def create_database():
  SQLModel.metadata.create_all(engine)
