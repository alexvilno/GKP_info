from .base import CRUDBase
from app.db_models import Persons
from app.schemas.persons import PersonsCreate, PersonsUpdate


class CRUDPersons(CRUDBase[Persons, PersonsUpdate, PersonsCreate]):
    pass


crud_persons = CRUDPersons(Persons)
