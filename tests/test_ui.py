import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUI:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        yield driver
        driver.quit()
    
    def test_home_page_loads(self, driver):
        driver.get("http://localhost:3000")
        assert "Тестовое приложение" in driver.title
        
        content = driver.find_element(By.ID, "content")
        assert content.text == "Основной контент"
        
        button = driver.find_element(By.ID, "test-button")
        assert button.is_displayed()
        assert button.text == "Тестовая кнопка"
    
    def test_page_structure(self, driver):
        driver.get("http://localhost:3000")
        
        # Проверяем наличие основных элементов
        heading = driver.find_element(By.TAG_NAME, "h1")
        assert heading.text == "Добро пожаловать в тестовое приложение"
        
        # Проверяем, что кнопка кликабельна
        button = driver.find_element(By.ID, "test-button")
        assert button.is_enabled()