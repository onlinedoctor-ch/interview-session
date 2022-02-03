from sys import prefix
from database.sql_database import SqlDatabase
from fastapi import FastAPI
from fastapi.logger import logger
from service.doctors import queries as doctor_queries


class Service(FastAPI):
    def __init__(self, *, db: SqlDatabase = None):
        self._db = db
        super().__init__(
            title="OnlineDoctor Data Service",
            description="This service provides data for the interview example",
            version="0.0.1",
            on_startup=[self._on_startup],
            on_shutdown=[self._on_shutdown],
        )

        self._setup_routes()

    def _on_startup(self) -> None:
        if self._db:
            self._db.wait_for_connection()

        logger.info("Starting application...")

    @staticmethod
    def _on_shutdown() -> None:
        logger.info("Shutting application down...")

    def _setup_routes(self) -> None:
        self.include_router(doctor_queries.router, prefix="/doctors")
