from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db

router = APIRouter()


@router.get(
    path="/persons"
)
def persons(
        db: Session = Depends(get_db)
):
    pass
