from fastapi import FastAPI
from routes.main import route
import uvicorn

class App():
  app = FastAPI()

  def start(self):
    self.app.include_router(route, prefix='/v1')
    uvicorn.run(self.app, host="0.0.0.0")
    return self.app