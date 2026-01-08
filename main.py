# Importing the neccessary dependencies and modules :

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import Optional, List 

# Initializing fastapi :
app = FastAPI(title="SQLAlchemy + FastAPI")

# Endpoints :

