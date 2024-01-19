from fastapi import FastAPI
from src.api.routes import routes

app = FastAPI()

app.include_router(routes)