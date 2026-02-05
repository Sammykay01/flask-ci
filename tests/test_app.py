from app import app

def test_home_returns_200():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert res.get_json()["message"] == "Hello from Flask CI!"
