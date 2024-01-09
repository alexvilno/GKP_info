from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.db import get_db

from app.schemas import PersonsCreate, PersonsBase, PersonsUpdate
from app.dal import crud_persons

router = APIRouter()


@router.post(
    path="/persons/create",
    response_model=PersonsBase
)
def persons(
    obj_in: PersonsCreate,
    db: Session = Depends(get_db)
):
    person = crud_persons.create(
        db=db,
        obj_in=obj_in
    )
    response = jsonable_encoder(person)
    return response


@router.post(
    path="/persons/update/{pers_id}",
    response_model=PersonsBase
)
def persons_update(
    pers_id: int,
    obj_in: PersonsUpdate,
    db: Session = Depends(get_db)
):
    person = crud_persons.get(db=db, req_id=pers_id)
    person = crud_persons.update(
        db=db,
        db_obj=person,
        obj_in=obj_in
    )
    response = jsonable_encoder(person)
    db.commit()
    return response
