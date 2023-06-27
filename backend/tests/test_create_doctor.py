import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def doctor_request() -> dict[str, str]:
    return {
        "first_name": "John",
        "last_name": "Smith",
        "specialization": "skin allergies",
    }


@pytest.mark.usefixtures("database_session")
def test_returns_201(client: TestClient, doctor_request: dict[str, str]) -> None:
    response = client.post("/doctors", json=doctor_request)
    assert response.status_code == 201


@pytest.mark.usefixtures("database_session")
def test_returns_data_that_includes_newly_created_doctor(
    client: TestClient, doctor_request: dict[str, str]
) -> None:
    response = client.post("/doctors", json=doctor_request)
    assert doctor_request.items() <= response.json().items()
