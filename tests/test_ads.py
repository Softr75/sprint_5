import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.login_locators import USER_AVATAR
from data.ad_data import AD_DATA

from locators.ads_locators import (
    PLACE_AD_BUTTON,
    AUTH_REQUIRED_MODAL_TEXT,
    TITLE_INPUT,
    CATEGORY_INPUT,
    HOBBY_CATEGORY_SPAN,
    CONDITION_OLD_RADIO,
    CITY_INPUT,
    NOVOSIBIRSK_CITY_SPAN,
    DESCRIPTION_INPUT,
    PRICE_INPUT,
    PUBLISH_BUTTON,
    EMPTY_TEXT_FIELD
)

class TestUserAds:
    def test_place_ad_by_unauthorized_user_shows_login_requirement(self, driver):
        driver.find_element(*PLACE_AD_BUTTON).click()

        modal_text = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AUTH_REQUIRED_MODAL_TEXT))
        assert modal_text.is_displayed()

    def test_place_ad_by_authorized_user_positive_result(self, logged_in_user):
        driver = logged_in_user
        wait = WebDriverWait(driver, 10)

        wait.until(expected_conditions.visibility_of_element_located(USER_AVATAR))

        place_ad_btn = wait.until(lambda d: d.find_element(*PLACE_AD_BUTTON))
        driver.execute_script("arguments[0].scrollIntoView(true);", place_ad_btn)
        driver.execute_script("arguments[0].click();", place_ad_btn)

        wait.until(expected_conditions.visibility_of_element_located(TITLE_INPUT))

        wait.until(expected_conditions.visibility_of_element_located(TITLE_INPUT)).send_keys(AD_DATA["title"])
        wait.until(expected_conditions.element_to_be_clickable(CATEGORY_INPUT)).click()
        wait.until(expected_conditions.element_to_be_clickable(HOBBY_CATEGORY_SPAN)).click()
        wait.until(expected_conditions.element_to_be_clickable(CONDITION_OLD_RADIO)).click()
        wait.until(expected_conditions.element_to_be_clickable(CITY_INPUT)).click()
        wait.until(expected_conditions.element_to_be_clickable(NOVOSIBIRSK_CITY_SPAN)).click()
        driver.execute_script("arguments[0].value = arguments[1];", driver.find_element(*DESCRIPTION_INPUT), AD_DATA["description"])
        wait.until(expected_conditions.visibility_of_element_located(PRICE_INPUT)).send_keys(AD_DATA["price"])
        wait.until(expected_conditions.element_to_be_clickable(PUBLISH_BUTTON)).click()

        driver.execute_script("window.scrollTo(0, 0);")
        empty_text = driver.find_elements(*EMPTY_TEXT_FIELD)
        assert len(empty_text) == 0
