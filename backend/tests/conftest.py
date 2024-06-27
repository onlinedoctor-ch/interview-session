import os
import pytest
from typing import Generator
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session, scoped_session

from database.sql_database import DatabaseBaseModel, SessionFactory, SqlDatabase
from service.main import create_app
from service.service import Service


@pytest.fixture(scope="session")
def database() -> SqlDatabase:
    database_url = os.environ.get("DATABASE_URL")
    db = SqlDatabase(url=database_url)
    db.wait_for_connection()
    return db


TestSession = scoped_session(session_factory=SessionFactory)


@pytest.fixture(scope="session")
def database_tables(database: SqlDatabase) -> Generator[None, None, None]:
    DatabaseBaseModel.metadata.reflect(bind=database.engine)
    DatabaseBaseModel.metadata.drop_all(bind=database.engine)
    DatabaseBaseModel.metadata.create_all(bind=database.engine)
    yield
    DatabaseBaseModel.metadata.drop_all(bind=database.engine)


@pytest.fixture(scope="function")
def database_session(
    database: SqlDatabase,
    database_tables: None,
) -> Generator[Session, None, None]:
    connection = database.engine.connect()
    transaction = connection.begin()
    TestSession.configure(bind=connection)
    test_session = TestSession()
    yield test_session
    TestSession.remove()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="session")
def app() -> Service:
    return create_app()


@pytest.fixture
def client(app: Service) -> TestClient:
    return TestClient(app)
