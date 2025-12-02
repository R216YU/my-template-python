from fastapi.testclient import TestClient

from app import app  # FastAPIアプリケーションインスタンス


class TestApp:
    def test_read_root(self):
        client = TestClient(app)
        response = client.get("/")

        assert response.status_code == 500
        assert response.json() == {"success": True, "message": "Hello, World!"}
