import os

PROJECT_APP = os.path.realpath(os.path.dirname(__file__)).replace('config', "")

settings = {
  "url_database" : f'sqlite:////{os.path.join(PROJECT_APP, "todo_database.db")}'
}

print(settings)