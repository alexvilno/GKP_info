from fastapi import APIRouter

from .endpoints import (
    persons
)

router_api_v1 = APIRouter()
router_api_v1.include_router(persons.router, tags=['persons'])
