from sqlalchemy.orm import Session

from . import schemas
from .models import users

def get_user(db: Session, user_id: int):
    return db.query(users.User).filter(users.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(users.User).filter(users.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(users.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = users.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user