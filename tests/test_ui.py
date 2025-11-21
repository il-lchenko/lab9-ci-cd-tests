import pytest
import requests

class TestUI:
    def test_home_page_content(self):
        """Простой тест содержимого страницы"""
        response = requests.get("http://localhost:3000/")
        assert response.status_code == 200
        # Более гибкие проверки
        html_content = response.text
        assert any(keyword in html_content for keyword in ['<h1>', '<div', '<button'])
        assert 'id="content"' in html_content
        assert 'id="test-button"' in html_content
    
    def test_page_structure(self):
        """Проверяем структуру страницы"""
        response = requests.get("http://localhost:3000/")
        assert response.status_code == 200
        # Проверяем что это HTML
        assert 'text/html' in response.headers.get('content-type', '')
        # Проверяем базовую структуру
        assert '<html' in response.text
        assert '<body' in response.text
        assert '</html>' in response.text