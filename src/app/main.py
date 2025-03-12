from fastapi import FastAPI
from app.routers import s3 as s3route


fapp = FastAPI()
fapp.include_router(s3route.router)
