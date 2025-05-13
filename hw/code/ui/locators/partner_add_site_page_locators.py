from selenium.webdriver.common.by import By

class PartnerAddSitePageLocators:
    LINK_TO_THE_SITE_INPUT = (By.XPATH, '//input[@placeholder="https://vk.com"]')
    INVALID_SITE_LINK_ERROR = (By.XPATH, '//*[contains(text(), "Ссылка должна указывать на действующий сайт")]')
    SITE_NAME_INPUT = (By.XPATH, '//input[@placeholder="Введите название сайта"]')
    EMPTY_SITE_NAME_ERROR = (By.XPATH, '//*[contains(text(), "Не может быть пустым")]')
    TOO_BIG_NAME_ERROR = (By.XPATH, '//*[contains(text(), "Название не должно превышать 200 символов")]')
    ADD_SITE_BUTTON = (By.XPATH, '//button[@data-testid="submit"]')
