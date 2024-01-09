from pydantic import Field, AliasChoices
from .base import Base


# Shared properties
class PersonsBase(Base):
    pers_name: str
    pers_surname: str | None = None
    pers_patronymic: str | None = None


# Properties on update
class PersonsUpdate(PersonsBase):
    pers_name: str | None = None


# Properties on create
class PersonsCreate(PersonsBase):
    pass


class PersonsInDBBase(PersonsBase):
    pers_id: int | None = Field(None, validation_alias=AliasChoices("id", "pers_id"), serialization_alias="id")
