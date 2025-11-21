import pytest
import requests

class TestUI:
    def test_home_page_content(self):
        """Простой тест содержимого страницы без Selenium"""
        response = requests.get("http://localhost:3000/")
        assert response.status_code == 200
        assert "Тестовое приложение" in response.text
        assert "Добро пожаловать" in response.text
    
    def test_page_elements_exist(self):
        """Проверяем что основные элементы присутствуют в HTML"""
        response = requests.get("http://localhost:3000/")
        html_content = response.text
        assert 'id="content"' in html_content
        assert 'id="test-button"' in html_content
        assert "<h1>" in html_content