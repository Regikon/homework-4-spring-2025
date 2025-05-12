from selenium.webdriver.common.by import By

class PartnerAddSitePageLocators:
    LINK_TO_THE_SITE_INPUT = (By.XPATH, '//input[@placeholder="https://vk.com"]')
    SITE_NAME_INPUT = (By.XPATH, '//input[@placeholder="Введите название сайта"]')
    ADD_SITE_BUTTON = (By.XPATH, '//button[contains(.,"Добавить сайт")]')
