from app.db import Base
from sqlalchemy import Column, String, Integer


class Persons(Base):
    __tablename__ = "PERSONS"

    pers_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    pers_name = Column(String, nullable=False)
    pers_surname = Column(String, nullable=True)
    pers_patronymic = Column(String, nullable=True)
