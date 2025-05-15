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

    FILTER_DROPDOWN = (By.XPATH, '//button[@data-testid="filter-buttons"]')
    STOPPED_FILTER = (By.XPATH, '//label[contains(@class, "vkuiCheckbox")][contains(., "Остановлено")]')
    ARCHIVED_FILTER = (By.XPATH, '//label[contains(@class, "vkuiCheckbox")][contains(., "В архиве")]')
    APPLY_FILTER_BUTTON = (By.XPATH, '//button[@data-testid="compact-filters-apply-button"]')

    ANY_ARCHIVED_SITE = (By.XPATH, '//*[@data-status="archived"]')

    SITE_SEARCH_INPUT = (By.XPATH, '//*[@class="vkuiSearch__input"]//input')

    NOTHING_FOUND_CAPTION = (By.XPATH, "//*[contains(concat(' ', normalize-space(@class), ' '), 'emptyView_title')]")
