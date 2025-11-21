import pytest
import requests

BASE_URL = "http://localhost:3000"

class TestAPI:
    def test_home_page(self):
        response = requests.get(f"{BASE_URL}/")
        assert response.status_code == 200
        assert "Тестовое приложение" in response.text
    
    def test_api_data(self):
        response = requests.get(f"{BASE_URL}/api/data")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert "data" in data
        assert data["data"]["id"] == 1
    
    def test_api_users(self):
        response = requests.get(f"{BASE_URL}/api/users")
        assert response.status_code == 200
        data = response.json()
        assert "users" in data
        assert len(data["users"]) == 2
        assert data["users"][0]["name"] == "Иван"
    
    def test_login_success(self):
        response = requests.post(
            f"{BASE_URL}/api/login",
            json={"username": "admin", "password": "password"}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert "token" in data
    
    def test_login_failure(self):
        response = requests.post(
            f"{BASE_URL}/api/login",
            json={"username": "wrong", "password": "wrong"}
        )
        assert response.status_code == 401
        data = response.json()
        assert data["status"] == "error"
    
    def test_not_found(self):
        response = requests.get(f"{BASE_URL}/api/nonexistent")
        assert response.status_code == 404
        data = response.json()
        assert data["status"] == "error"