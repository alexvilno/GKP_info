from typing import TypeVar, Any, Generic, Type, Optional, Union, Dict
from app.schemas import Base as BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import SQLColumnExpression
from fastapi.encoders import jsonable_encoder
from sqlite3 import Error

ModelType = TypeVar("ModelType", bound=Any)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, req_id) -> Optional[ModelType]:
        return db.query(self.model).get(req_id)

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        try:
            obj_data = jsonable_encoder(db_obj)
            if isinstance(obj_in, dict):
                update_data = obj_in
            else:
                update_data = obj_in.model_dump(exclude_unset=True)
            for field in obj_data:
                if field in update_data:
                    setattr(db_obj, field, update_data[field])
            db.add(db_obj)
            db.flush()
            db.refresh(db_obj)
            return db_obj
        except Error as err:
            raise err
        except Exception as err:
            raise err

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        try:
            obj_in_data = jsonable_encoder(obj_in)
            if isinstance(obj_in, dict):
                create_data = obj_in_data
            else:
                create_data = obj_in.model_dump(exclude_unset=True)
            db_obj = self.model(**create_data)
            db.add(db_obj)
            db.flush()
            db.refresh(db_obj)
            return db_obj

        except Error as err:
            raise err

        except Exception as err:
            raise err

    def remove(self, db: Session, *, req_id: int) -> ModelType:
        try:
            obj = db.query(self.model).get(req_id)
            db.delete(obj)
            db.flush()
            return obj
        except Error as err:
            raise err

        except Exception as err:
            raise err

    def get_by_criterion(self, db: Session, *, criterion: SQLColumnExpression) -> list[ModelType]:
        return db.query(self.model).filter(criterion).all()

    def get_by_criteria(self, db: Session, *, criteria: list[SQLColumnExpression]) -> list[ModelType]:
        query = db.query(self.model)
        for criterion in criteria:
            query = query.filter(criterion)
        return query.all()
