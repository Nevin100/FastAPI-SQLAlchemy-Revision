from fastapi import FastAPI
from app.database.db import engine
from app.models import user
from app.routes.routes import router as user_router

# Create Tables :
user.Base.metadata.create_all(bind=engine)

# Initilizing FastAPI :
app = FastAPI(title="FastAPI + SQLAlchemy REST APIs")

# Routes Registeration : 
app.include_router(user_router)

