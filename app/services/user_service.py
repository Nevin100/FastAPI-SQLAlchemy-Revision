from sqlalchemy.orm import Session 
from models.user import User
from schemas.user import UserCreate

# Create User :
def create_user(db: Session, user: UserCreate):
    # check whether the user exists or not :
    existing_user = (
        db.query(User).filter(User.email == user.email).first()
    )

    # if user exists -> return none
    if existing_user:
        return None
    
    # if not exist:
    db_user = User(
        name = user.name,
        email = user.email
    )

    # DB Operations :
    # Add in Session :
    db.add(db_user)

    # Permanently Saving :
    db.commit()

    # Refresh the Updated Data :
    db.refresh(db_user)

    return db_user


# Get All Users : 
def get_all_users(db : Session):
    return db.query(User).all()

# Get Single User :
def get_single_user(db: Session, user_id : int):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return None

    return user

# Delete user : 
def delete_user(db: Session, user_id: int):
    
    # check whether the user exists or not : 
    existing_user = db.query(User).filter(User.id == user_id).first()

    if not existing_user:
        return None
    
    # DB Delete Operations
    # Delete Operation :
    db.delete(existing_user)

    db.commit()
    return existing_user

#

    