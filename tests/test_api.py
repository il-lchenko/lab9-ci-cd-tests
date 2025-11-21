import pytest
import requests
import time
import subprocess
import os

class TestAPI:
    @classmethod
    def setup_class(cls):
        """Запускаем сервер перед всеми тестами"""
        print("Starting server...")
        cls.server_process = subprocess.Popen(["node", "server.js"])
        time.sleep(3)  # Даем серверу время на запуск
    
    @classmethod
    def teardown_class(cls):
        """Останавливаем сервер после всех тестов"""
        print("Stopping server...")
        cls.server_process.terminate()
        cls.server_process.wait()

    def test_home_page(self):
        response = requests.get("http://localhost:3000/")
        assert response.status_code == 200
        assert "Welcome" in response.text
        assert "Test Application" in response.text
    
    def test_api_data(self):
        response = requests.get("http://localhost:3000/api/data")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert "data" in data
        assert data["data"]["id"] == 1
    
    def test_api_users(self):
        response = requests.get("http://localhost:3000/api/users")
        assert response.status_code == 200
        data = response.json()
        assert "users" in data
        assert len(data["users"]) == 2
    
    def test_login_success(self):
        response = requests.post(
            "http://localhost:3000/api/login",
            json={"username": "admin", "password": "password"}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert "token" in data
    
    def test_login_failure(self):
        response = requests.post(
            "http://localhost:3000/api/login",
            json={"username": "wrong", "password": "wrong"}
        )
        assert response.status_code == 401
        data = response.json()
        assert data["status"] == "error"
    
    def test_not_found(self):
        response = requests.get("http://localhost:3000/api/nonexistent")
        assert response.status_code == 404
        data = response.json()
        assert data["status"] == "error"