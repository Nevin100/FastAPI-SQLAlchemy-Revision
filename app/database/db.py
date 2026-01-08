# importing the SQLAlchemy and all neccessary requirements essential for the database connection

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATBASE_URL = "sqlite:///./test.db"

# create_engine() : It forms the connection with Database
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} # SQLITE spcific
)

# Session for Database Crud Operations :
# sessionmaker() : It forms a session to operate with a database
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for all models
# declarative_base() : it is a base class use to define tables
Base = declarative_base()

def get_DB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()