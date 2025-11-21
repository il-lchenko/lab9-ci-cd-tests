import pytest
import requests
import time
import subprocess
import os

def setup_module(module):
    """Запускаем сервер перед всеми тестами"""
    print("🚀 Starting server...")
    # Запускаем сервер в фоновом режиме
    global server_process
    server_process = subprocess.Popen(["node", "server.js"], 
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
    
    # Ждем пока сервер запустится
    time.sleep(3)
    
    # Проверяем что сервер работает
    max_attempts = 10
    for i in range(max_attempts):
        try:
            response = requests.get("http://localhost:3000/", timeout=5)
            if response.status_code == 200:
                print("✅ Server is ready!")
                return
        except:
            if i == max_attempts - 1:
                raise Exception("❌ Server failed to start")
            time.sleep(1)

def teardown_module(module):
    """Останавливаем сервер после всех тестов"""
    print("🛑 Stopping server...")
    global server_process
    if server_process:
        server_process.terminate()
        server_process.wait()

class TestAPI:
    def test_home_page(self):
        response = requests.get("http://localhost:3000/")
        assert response.status_code == 200
        assert "Test Application" in response.text
    
    def test_api_data(self):
        response = requests.get("http://localhost:3000/api/data")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert "data" in data
    
    def test_api_users(self):
        response = requests.get("http://localhost:3000/api/users")
        assert response.status_code == 200
        data = response.json()
        assert "users" in data
        assert len(data["users"]) == 2
    
    def test_login(self):
        response = requests.post(
            "http://localhost:3000/api/login",
            json={"username": "admin", "password": "password"}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
    
    def test_not_found(self):
        response = requests.get("http://localhost:3000/api/nonexistent")
        assert response.status_code == 404

class TestUI:
    def test_home_page_content(self):
        response = requests.get("http://localhost:3000/")
        assert response.status_code == 200
        html = response.text
        assert "<h1>" in html
        assert 'id="content"' in html
        assert 'id="test-button"' in html
    
    def test_page_structure(self):
        response = requests.get("http://localhost:3000/")
        assert response.status_code == 200
        assert "text/html" in response.headers.get("content-type", "")