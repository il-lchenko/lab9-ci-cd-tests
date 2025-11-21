import pytest
import requests
import time
import subprocess
import os

@pytest.fixture(scope="session", autouse=True)
def start_server():
    # Запускаем сервер в фоновом режиме
    server_process = subprocess.Popen(["node", "server.js"], 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.PIPE)
    
    # Ждем пока сервер запустится
    time.sleep(2)
    
    # Проверяем что сервер работает
    max_attempts = 10
    for attempt in range(max_attempts):
        try:
            response = requests.get("http://localhost:3000/", timeout=5)
            if response.status_code == 200:
                print("Сервер успешно запущен")
                break
        except:
            if attempt == max_attempts - 1:
                raise Exception("Не удалось запустить сервер")
            time.sleep(1)
    
    yield
    
    # Останавливаем сервер после выполнения всех тестов
    server_process.terminate()
    server_process.wait()