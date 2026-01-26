from selenium.webdriver.common.by import By

PLACE_AD_BUTTON = (By.XPATH, "//button[contains(@class, 'buttonPrimary') and text()='Разместить объявление']")
AUTH_REQUIRED_MODAL_TEXT = (By.XPATH,"//div[contains(@class,'popUp_titleRow')]//*[contains(text(),'авторизуйтесь')]")
TITLE_INPUT = (By.NAME, "name")
CATEGORY_INPUT = (By.XPATH, "//input[@name='category']/following-sibling::button[contains(@class, 'dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP')]//*[local-name()='svg']")
HOBBY_CATEGORY_SPAN = (By.XPATH, "//span[text()='Хобби']")
CONDITION_OLD_RADIO = (By.XPATH, "//input[@value='Б/У']/following-sibling::*[contains(@class,'radioUnput_inputRegular__FbVbr')]")
CITY_INPUT = (By.XPATH, "//input[@name='city']/following-sibling::button[contains(@class, 'dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP')]//*[local-name()='svg']")
NOVOSIBIRSK_CITY_SPAN = (By.XPATH, "//span[text()='Новосибирск']")
DESCRIPTION_INPUT = (By.NAME, "description")
PRICE_INPUT = (By.NAME, "price")
PUBLISH_BUTTON = (By.XPATH, "//button[contains(@class, 'buttonPrimary') and text()='Опубликовать']")
EMPTY_TEXT_FIELD = (By.XPATH,"//div[contains(@class, 'profilePage_listningBlock')][.//h1[text()='Мои объявления']]//h2[text()='Здесь пока пусто...']")