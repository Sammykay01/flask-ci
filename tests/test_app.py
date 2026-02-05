from app import create_app

def test_home_returns_200():
    app = create_app()
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert res.get_json()["message"] == "Hello from Flask CI!"

