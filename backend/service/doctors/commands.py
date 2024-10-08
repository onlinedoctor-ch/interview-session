from fastapi import APIRouter, Body, Depends, Path
from sqlalchemy.orm.session import Session
from starlette import status
from starlette.responses import Response

from database.sql_database import db_session
from service.doctors.models import BaseDoctor, Doctor, DoctorOrm

router = APIRouter()


class DoctorCreate(BaseDoctor):
    pass


@router.post("/doctors", status_code=201)
def create_doctor(
    doctor: DoctorCreate = Body(default=...),
    db: Session = Depends(db_session),
) -> Doctor:
    new_doctor = DoctorOrm(**doctor.dict())
    db.add(new_doctor)
    db.commit()
    return Doctor.from_orm(new_doctor)


@router.delete("/doctors/{doctor_id}", status_code=204)
def delete_doctor(
    doctor_id: int = Path(default=...),
    db: Session = Depends(db_session),
) -> Response:
    db.query(DoctorOrm).filter(DoctorOrm.id == doctor_id).delete()
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
