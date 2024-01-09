from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db

from app.db_models import Persons

router = APIRouter()


@router.get(
    path="/persons"
)
def persons(
        db: Session = Depends(get_db)
):
    q = db.query(Persons).get(1)
    return q.__dict__
