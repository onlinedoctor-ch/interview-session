from dataclasses import Field
from doctest import Example
from pydantic import BaseModel, Field
from database.sql_database import DatabaseBaseModel
from sqlalchemy import Column, Integer, String

class DoctorOrm(DatabaseBaseModel):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    specialization = Column(String(50), nullable=True)

class BaseDoctor(BaseModel):
    first_name: str = Field(..., example="Marie")
    last_name: str = Field(..., example="Curie")
    specialization: str = Field(..., example="Skin Cancer")

class Doctor(BaseDoctor):
    id: int

    class Config:
        orm_mode = True 


