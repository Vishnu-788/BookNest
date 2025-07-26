from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from app.core.config import get_settings

settings = get_settings()
Base = declarative_base()  # use this one for all models

engine = create_engine(settings.db_url, connect_args={"check_same_thread": False})

Sessionlocal = sessionmaker(bind=engine)


# use this function to get access to the db
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
