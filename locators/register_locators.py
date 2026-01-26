from selenium.webdriver.common.by import By

NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(@class, 'buttonSecondary') and text()='Нет аккаунта']")
SUBMIT_PASSWORD_INPUT = (By.NAME, 'submitPassword')
CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(@class, 'buttonPrimary') and text()='Создать аккаунт']")
