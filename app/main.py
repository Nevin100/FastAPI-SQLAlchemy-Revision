from fastapi import FastAPI
from database.db import engine
from models import user
from routes.routes import router as user_router

# Create Tables :
user.Base.metadata.create_all(bind=engine)

# Initilizing FastAPI :
app = FastAPI(title="FastAPI + SQLAlchemy REST APIs")

# Routes Registeration : 
app.include_router(user_router)

