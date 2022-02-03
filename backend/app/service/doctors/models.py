from pydantic import BaseModel

class Doctor(BaseModel):
    first_name: str
    last_name: str
    specialization: str