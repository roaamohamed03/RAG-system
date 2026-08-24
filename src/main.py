from fastapi import FastAPI
from src.routes.root import root_router

app = FastAPI()

app.include_router(root_router)
