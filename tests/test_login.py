import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data.auth_data import EXISTING_EMAIL, EXISTING_PASSWORD
from config import LOGIN_URL

from locators.login_locators import (
    LOG_AND_REG_BUTTON,
    EMAIL_INPUT,
    PASSWORD_INPUT,
    LOGIN_BUTTON,
    USER_AVATAR,
    USER_NAME
)

class TestUserLogin:
    def test_successful_user_login(self, driver):
        driver.find_element(*LOG_AND_REG_BUTTON).click()

        email_input = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(EMAIL_INPUT))
        email_input.send_keys(EXISTING_EMAIL)
        driver.find_element(*PASSWORD_INPUT).send_keys(EXISTING_PASSWORD)
        driver.find_element(*LOGIN_BUTTON).click()

        assert driver.current_url == LOGIN_URL
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(USER_AVATAR))
        
        assert driver.find_element(*USER_AVATAR).is_displayed()
        assert driver.find_element(*USER_NAME).text == "User."
        