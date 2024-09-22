from config.setting import settings
from sqlmodel import create_engine, SQLModel
import models.Todo

engine = create_engine(settings.get("url_database"), echo=True)

def create_database():
  SQLModel.metadata.create_all(engine)
