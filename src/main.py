from fastapi import FastAPI
from api.routes import routes

app = FastAPI()

app.include_router(routes)