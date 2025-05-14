from selenium.webdriver.common.by import By

class AudienceAddAudiencePageLocators:
    ADD_SOURCE_BUTTON = (By.XPATH, '//button[contains(.,"Добавить источник")]')
    EXCLUDE_SOURCE_BUTTON = (By.XPATH, '//button[contains(.,"Исключить источник")]')

    USERLIST_SOURCE_BUTTON = (By.XPATH, '//div[contains(@class, "SourceType_button")][.//*[contains(., "Список пользователей")]]')