from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.db import get_DB
from app.schemas.user import UserCreate, UserResponse
from app.services import user_service

# APIRouter
router = APIRouter(prefix="/users", tags=["Users"])

# Create User : 
@router.post("/create-user", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, db: Session = Depends(get_DB)):
    user = user_service.create_user(
        db = db,
        user = payload
    )

    if user is None:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail="user already exists")
    
    return user

# Get All Users : 
@router.get("/get-users", response_model= list[UserResponse], status_code=status.HTTP_200_OK)
def get_all_users(db: Session = Depends(get_DB)):
    user = user_service.get_all_users(db = db)

    return user
 

# Get By Single ID : 
@router.get("/get-user/{id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_single_book( id : int, db: Session = Depends(get_DB)):
    user = user_service.get_single_user(db = db, user_id = id)

    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No user exists in Database")
    
    return user

# Update User :
@router.put("/update-user/{id}", response_model=UserResponse, status_code = status.HTTP_200_OK)
def update_user(payload: UserCreate, id:int,db: Session = Depends(get_DB),):
    user = user_service.update_user(db = db, user_id=id, user = payload)

    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="No user exists in Database")
    
    return user

# Delete User :
@router.delete("/delete-user/{id}", response_model=UserResponse, status_code = status.HTTP_200_OK)
def delete_user( id: int,db : Session = Depends(get_DB)):
    user = user_service.delete_user(db = db, user_id = id)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user exists in Database")
    
    return {    
        "detail":"User Deleted Successfully",
    }