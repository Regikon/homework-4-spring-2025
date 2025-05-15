from selenium.webdriver.common.by import By

class PartnerSiteAdBlocksPageLocators:
    ADD_AD_BLOCK_BUTTON = (By.XPATH, '//button[contains(., "Добавить блок")]')

    @staticmethod
    def BLOCK_ENTRY(id: int):
        return (By.XPATH, f'//div[@data-entityid][contains(., "{id}")]')

    # We cannot find checkbox by id, it is impossible due to the page layout
    @staticmethod
    def BLOCK_CHECKBOX(name: str):
        return (By.XPATH, f'//div[@data-entityid][contains(., "{name}")]//input[@type="checkbox"]/following-sibling::div')

    @staticmethod
    def BLOCK_STATUS(id: int):
        return (By.XPATH, f'//div[@data-entityid][contains(., "{id}")]//*[@data-status]')

    ACTIONS_DROPDOWN = (By.XPATH, '//button[@data-testid="select-options"]')

    ARCHIVE_OPTION = (By.XPATH, '//*[@role="button"][contains(., "Архивировать")]')
    STOP_OPTION = (By.XPATH, '//*[@role="button"][contains(., "Остановить")]')

    CLEAR_ALL_BUTTON = (By.XPATH, '//button[contains(., "Очистить все")]')

    FILTER_DROPDOWN = (By.XPATH, '//button[@data-testid="filter-buttons"]')
    STOPPED_FILTER = (By.XPATH, '//label[contains(@class, "vkuiCheckbox")][contains(., "Остановлено")]')
    ARCHIVED_FILTER = (By.XPATH, '//label[contains(@class, "vkuiCheckbox")][contains(., "В архиве")]')
    APPLY_FILTER_BUTTON = (By.XPATH, '//button[@data-testid="compact-filters-apply-button"]')

    ANY_ARCHIVED_BLOCK = (By.XPATH, '//*[@data-status="archived"]')

    BLOCK_SEARCH_INPUT = (By.XPATH, '//input[@data-testid="search"]')

    NOTHING_FOUND_CAPTION = (By.XPATH, "//*[contains(concat(' ', normalize-space(@class), ' '), 'emptyView_title')]")

    @staticmethod
    def DUPLICATE_BLOCK_BUTTON(id: int):
        return (By.XPATH, f"//*[@data-entityid][contains(.,'{id}')]//*[contains(@aria-label, 'Copy')]")

    CONFIRM_DUPLICATE_BUTTON = (By.XPATH, '//button[contains(., "Дублировать")]')
