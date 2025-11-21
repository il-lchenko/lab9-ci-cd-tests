import pytest
import requests
import time
import subprocess
import os

@pytest.fixture(scope="session", autouse=True)
def start_server():
    # Запускаем сервер
    print("Запускаем тестовый сервер...")
    server_process = subprocess.Popen(["node", "server.js"])
    
    # Даем серверу время на запуск
    time.sleep(3)
    
    # Проверяем что сервер работает
    try:
        response = requests.get("http://localhost:3000/", timeout=10)
        if response.status_code == 200:
            print("✅ Сервер успешно запущен")
        else:
            print("❌ Сервер не отвечает корректно")
    except Exception as e:
        print(f"❌ Ошибка подключения к серверу: {e}")
    
    yield
    
    # Останавливаем сервер
    print("Останавливаем сервер...")
    server_process.terminate()
    server_process.wait()