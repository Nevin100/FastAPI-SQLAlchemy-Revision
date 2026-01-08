from sqlalchemy import Column , Integer , String
from database.db import Base

# Table Definition (using class)
class User(Base):

    # Table Name :
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index = True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index = True)
    