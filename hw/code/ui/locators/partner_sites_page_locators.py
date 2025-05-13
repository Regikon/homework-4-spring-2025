from selenium.webdriver.common.by import By

class PartnerSitesPageLocators:
    ADD_SITE_BUTTON = (By.XPATH, '//button[contains(.,"Добавить сайт")]')
    
    @staticmethod
    def SITE_ENTRY(id: int):
        return (By.XPATH, f'//div[@data-entityid={id}]')
