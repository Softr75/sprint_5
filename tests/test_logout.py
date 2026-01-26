import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver

from locators.login_locators import (
    LOGOUT_BUTTON,
    USER_AVATAR,
    USER_NAME,
    LOG_AND_REG_BUTTON
)

class TestUserLogout:
    def test_successful_user_logout(self, logged_in_user):
        driver = logged_in_user

        logout_btn = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(LOGOUT_BUTTON))
        logout_btn.click()

        login_btn = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LOG_AND_REG_BUTTON))

        assert login_btn.is_displayed()
        assert len(driver.find_elements(*USER_AVATAR)) == 0
        assert len(driver.find_elements(*USER_NAME)) == 0
