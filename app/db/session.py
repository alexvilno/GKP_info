from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os.path

SQLITE_DATABASE_URL = f"sqlite:///{os.path.dirname(os.path.abspath(__file__))}/sqlitedb.db"

engine = create_engine(
    SQLITE_DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
