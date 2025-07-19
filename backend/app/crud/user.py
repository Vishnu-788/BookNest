from sqlalchemy.orm import Session
from app import models, schemas

def get_user_by_username(username: str, db: Session):
    return db.query(models.user.User).filter(models.user.User.username == username).first()

def get_user_by_email(email: str, db: Session):
    return db.query(models.user.User).filter(models.user.User.email == email).first()

def create(request: schemas.user.UserCreate, db: Session):
    new_user = models.user.User(**request.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user