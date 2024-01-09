from pydantic import Field, AliasChoices
from .base import Base


class PersonBase(Base):
    pers_id: int | None = Field(None, validation_alias=AliasChoices("id", "pers_id"), serialization_alias="id")
    pers_name: str
    pers_surname: str | None = None
    pers_patronymic: str | None = None
