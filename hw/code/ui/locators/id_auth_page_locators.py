from selenium.webdriver.common.by import By

class IdAuthPageLocators:
    TELEPHONE = (By.XPATH, '//input[@placeholder="Телефон или почта"]')
    CONTINUE_LOGIN = (By.XPATH, '//button[type="submit"]')
    ACCOUNT = (By.XPATH, '//div[span[text()="Физическое лицо"]]')