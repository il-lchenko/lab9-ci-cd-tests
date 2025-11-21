import pytest
import requests
import time
import subprocess
import os

@pytest.fixture(scope="session", autouse=True)
def start_server():
    # Проверяем, не запущен ли уже сервер
    try:
        response = requests.get("http://localhost:3000/", timeout=2)
        if response.status_code == 200:
            print("✅ Сервер уже запущен")
            yield
            return
    except:
        pass
    
    # Запускаем сервер только если он не запущен
    print("🚀 Запускаем тестовый сервер...")
    server_process = subprocess.Popen(["node", "../server.js"])
    
    # Ждем запуска сервера
    max_attempts = 10
    for attempt in range(max_attempts):
        try:
            response = requests.get("http://localhost:3000/", timeout=5)
            if response.status_code == 200:
                print("✅ Сервер успешно запущен")
                break
        except Exception as e:
            if attempt == max_attempts - 1:
                print(f"❌ Не удалось запустить сервер: {e}")
                raise
            time.sleep(1)
    
    yield
    
    # Останавливаем сервер
    print("🛑 Останавливаем сервер...")
    server_process.terminate()
    server_process.wait()