import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers.email_generator import generate_email
from data.auth_data import (
    EXISTING_EMAIL,
    EXISTING_PASSWORD,
    INVALID_EMAIL
)

from locators.login_locators import (
    LOG_AND_REG_BUTTON,
    EMAIL_INPUT,
    PASSWORD_INPUT,
    USER_AVATAR,
    USER_NAME,
    ERROR_SPAN
)

from locators.register_locators import(
    NO_ACCOUNT_BUTTON,
    SUBMIT_PASSWORD_INPUT,
    CREATE_ACCOUNT_BUTTON
)

class TestUserRegistration:

    def test_successful_user_registration(self, driver):
        email = generate_email()
        driver.find_element(*LOG_AND_REG_BUTTON).click()
        driver.find_element(*NO_ACCOUNT_BUTTON).click()

        driver.find_element(*EMAIL_INPUT).send_keys(email)
        driver.find_element(*PASSWORD_INPUT).send_keys("Password123!")
        driver.find_element(*SUBMIT_PASSWORD_INPUT).send_keys("Password123!")
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(USER_AVATAR))

        assert driver.find_element(*USER_AVATAR).is_displayed()
        assert driver.find_element(*USER_NAME).text == "User."

    def test_registration_invalid_email_shows_error(self, driver):
        driver.find_element(*LOG_AND_REG_BUTTON).click()
        driver.find_element(*NO_ACCOUNT_BUTTON).click()

        driver.find_element(*EMAIL_INPUT).send_keys(INVALID_EMAIL)
        driver.find_element(*PASSWORD_INPUT).send_keys("Password123!")
        driver.find_element(*SUBMIT_PASSWORD_INPUT).send_keys("Password123!")
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

        error_message = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(ERROR_SPAN))
        assert error_message.is_displayed()

        for locator in [EMAIL_INPUT, PASSWORD_INPUT, SUBMIT_PASSWORD_INPUT]:
            error_input = driver.find_element(*locator).find_element(By.XPATH, "..")
            assert "Error" in error_input.get_attribute("class")

    def test_registration_existing_user_shows_error(self, driver):
        driver.find_element(*LOG_AND_REG_BUTTON).click()
        driver.find_element(*NO_ACCOUNT_BUTTON).click()

        driver.find_element(*EMAIL_INPUT).send_keys(EXISTING_EMAIL)
        driver.find_element(*PASSWORD_INPUT).send_keys(EXISTING_PASSWORD)
        driver.find_element(*SUBMIT_PASSWORD_INPUT).send_keys(EXISTING_PASSWORD)
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

        error_message = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(ERROR_SPAN))
        assert error_message.is_displayed()

        for locator in [EMAIL_INPUT, PASSWORD_INPUT, SUBMIT_PASSWORD_INPUT]:
            error_input = driver.find_element(*locator).find_element(By.XPATH, "..")
            assert "Error" in error_input.get_attribute("class")
