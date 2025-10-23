import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    return app.test_client()


def test_index_route(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"HELLO WORLD" in res.data


def test_healthz(client):
    res = client.get("/healthz")
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}
