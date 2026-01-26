from selenium.webdriver.common.by import By

LOG_AND_REG_BUTTON = (By.XPATH, "//button[contains(@class, 'buttonSecondary') and text()='Вход и регистрация']")
EMAIL_INPUT = (By.NAME, 'email')
PASSWORD_INPUT = (By.NAME, 'password')
LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'buttonPrimary') and text()='Войти']")
LOGOUT_BUTTON = (By.XPATH, ".//button[contains(@class,'spanGlobal') and contains(@class,'btnSmall')]")
USER_AVATAR = (By.XPATH, ".//button[@class='circleSmall']")
USER_NAME = (By.XPATH, ".//*[@class='profileText name']")
ERROR_SPAN = (By.XPATH, ".//*[contains(@class, 'input_span__yWPqB') and contains(text(), 'Ошибка')]")
