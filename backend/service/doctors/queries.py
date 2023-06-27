from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm.session import Session

from database.sql_database import db_session
from service.doctors.models import BaseDoctor
from service.doctors.models import DoctorOrm
from service.doctors.models import Doctor

router = APIRouter()


class HealthCheck(BaseModel):
    status: str


class DoctorCreate(BaseDoctor):
    pass


@router.get("/doctors")
def get_doctors(db: Session = Depends(db_session)) -> list[Doctor]:
    doctors = [
        Doctor.from_orm(db_doctor)
        for db_doctor in db.query(DoctorOrm).order_by(DoctorOrm.id.desc()).all()
    ]
    return doctors
