from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HealthCheck(BaseModel):
    status: str


@router.get("/health", response_model=HealthCheck)
def get_health() -> HealthCheck:
    print("I am ok")
    return HealthCheck(status="OK")
