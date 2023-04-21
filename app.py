from fastapi import FastAPI
from routes.app import routes

app = FastAPI()
app.include_router(routes)