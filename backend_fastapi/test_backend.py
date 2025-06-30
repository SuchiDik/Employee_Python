# Test cases for FastAPI backend

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

headers = {"Authorization": "Bearer mysecrettoken"}


def test_create_and_read_employee():
    data = {
        "name": "Test User",
        "department": "Testing",
        "email": "testuser@example.com"
    }


response = client.post("/employees/", json=data, headers=headers)
assert response.status_code == 200
emp_id = response.json()["id"]

response = client.get(f"/employees/{emp_id}", headers=headers)
assert response.status_code == 200
assert response.json()["name"] == "Test User"


def test_list_employees():
    response = client.get("/employees/?skip=0&limit=5", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)