from fastapi import FastAPI
import app.routers


fapp = FastAPI()
fapp.include_router(app.routers.s3.router)
