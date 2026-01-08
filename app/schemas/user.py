from pydantic import BaseModel, EmailStr

# Request schema (POST / PUT)
class UserCreate(BaseModel):
    name: str
    email: EmailStr

# Response schema
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    # SQLAlchemy Object is converted to pydantic Object
    class Config:
        from_attributes = True      
