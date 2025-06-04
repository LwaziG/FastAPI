from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import user
from users import schemas
import hashlib

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user after validating uniqueness of email and username.
    Password is hashed using SHA-256 before storage.
    """
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already taken")
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_pw = hashlib.sha256(user.password.encode()).hexdigest()
    db_user = User(username=user.username, email=user, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    """
    Retrieve and return a list of all registered users.
    """
    return db.query(User).all()


@router.get("/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single user by their ID.
    Raises 404 if the user is not found.
    """
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user