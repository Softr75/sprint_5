import os
import pytest
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data.auth_data import EXISTING_EMAIL, EXISTING_PASSWORD
from config import BASE_URL
from locators.login_locators import (
    LOG_AND_REG_BUTTON,
    EMAIL_INPUT,
    PASSWORD_INPUT,
    LOGIN_BUTTON
)   

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chromedriver_path = os.path.join(os.path.dirname(__file__), "drivers", "chromedriver.exe")
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_user(driver):
    driver.find_element(*LOG_AND_REG_BUTTON).click()
    email_input = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(EMAIL_INPUT))
    email_input.send_keys(EXISTING_EMAIL)
    driver.find_element(*PASSWORD_INPUT).send_keys(EXISTING_PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()
    yield driver