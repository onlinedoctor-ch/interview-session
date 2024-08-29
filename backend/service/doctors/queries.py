from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from database.sql_database import db_session
from service.doctors.models import Doctor, DoctorOrm

router = APIRouter()


@router.get("/doctors")
def get_doctors(db: Session = Depends(db_session)) -> list[Doctor]:
    doctors = [
        Doctor.from_orm(db_doctor)
        for db_doctor in db.query(DoctorOrm).order_by(DoctorOrm.id.desc()).all()
    ]
    return doctors
