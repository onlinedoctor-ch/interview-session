import os

from database.sql_database import SqlDatabase
from fastapi.middleware.cors import CORSMiddleware
from service.doctors.models import Doctor

from service.service import Service


def create_app() -> Service:
    database = SqlDatabase(url=os.environ.get("DATABASE_URL"))
    app = Service(db=database)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app
