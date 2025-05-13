from selenium.webdriver.common.by import By

class PartnerSitesPageLocators:
    ADD_SITE_BUTTON = (By.XPATH, '//button[contains(.,"Добавить сайт")]')
    
    @staticmethod
    def SITE_ENTRY(id: int):
        return (By.XPATH, f'//div[@data-entityid={id}]')

    @staticmethod
    def SITE_CHECKBOX(id: int):
        return (By.XPATH, f'//div[@data-entityid={id}]//input[@type="checkbox"]/following-sibling::div')

    @staticmethod
    def SITE_STATUS(id: int):
        return (By.XPATH, f'//div[@data-entityid={id}]//*[@data-status]')

    ACTIONS_DROPDOWN = (By.XPATH, '//button[@data-testid="select-options"]')

    ARCHIVE_OPTION = (By.XPATH, '//*[@role="button"][contains(., "Архивировать")]')
    STOP_OPTION = (By.XPATH, '//*[@role="button"][contains(., "Остановить")]')

    CLEAR_ALL_BUTTON = (By.XPATH, '//button[contains(., "Очистить все")]')
