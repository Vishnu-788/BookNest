from sqlalchemy.orm import Session
from app import models, schemas


def get_user_by_username(username: str, db: Session):
    return (
        db.query(models.user.User).filter(models.user.User.username == username).first()
    )


def get_user_by_email(email: str, db: Session):
    return db.query(models.user.User).filter(models.user.User.email == email).first()


def create(user_data: schemas.auth.UserCreate, db: Session):
    new_user = models.user.User(**user_data.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def create_member(member_data, db: Session):
    new_member = models.user.MemberDetails(**member_data.model_dump())
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    return new_member

def create_librarian(member_data, db: Session):
    new_member = models.user.LibrarianDetails(**member_data.model_dump())
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    return new_member