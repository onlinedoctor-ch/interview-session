import threading
from datetime import datetime
from time import sleep
from typing import Generator
from urllib.parse import urlparse

import psycopg2
from fastapi.logger import logger
from psycopg2._psycopg import OperationalError
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base, Session, sessionmaker

SessionFactory = sessionmaker(autocommit=False, autoflush=False)
DatabaseBaseModel = declarative_base()


class SqlDatabase:
    def __init__(self, url: str):
        self.url = url
        parsed_url = urlparse(self.url)
        self.username = parsed_url.username
        self.password = parsed_url.password
        self.database_name = parsed_url.path[1:]
        self.hostname = parsed_url.hostname
        self.port = parsed_url.port
        logger.info("Creating database engine")
        self._engine: Engine = create_engine(self.url, pool_pre_ping=True)
        SessionFactory.configure(bind=self._engine)

    def _test_connection(self) -> None:
        connection = psycopg2.connect(
            database=self.database_name,
            user=self.username,
            password=self.password,
            host=self.hostname,
            port=self.port,
        )
        connection.close()

    def _wait_until_ready(self) -> None:
        logger.info(f"Database URL: {self.url}")
        logger.info("Waiting for database connection...")
        start_time = datetime.now()
        while True:
            try:
                self._test_connection()
                logger.info("Database connection established.")
                return
            except OperationalError:
                logger.warning("Unable to connect to database, retrying")
                elapsed_time = datetime.now() - start_time

                if elapsed_time.total_seconds() > 60:
                    logger.error(
                        "Could not connect to the database, exiting application."
                    )
                    exit(1)

                sleep(1)

    def wait_for_connection(self) -> None:
        thread = threading.Thread(target=self._wait_until_ready)
        thread.start()
        thread.join()

    @property
    def engine(self) -> Engine:
        return self._engine


def db_session() -> Generator[Session, None, None]:
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()
