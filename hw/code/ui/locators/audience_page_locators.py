from selenium.webdriver.common.by import By

class AudiencePageLocators:
    @staticmethod
    def USERLIST_BY_NAME(name: str):
        return (By.XPATH, f'//div[@id="audience.users_list"]//div[contains(@class, "EditableName_nameValue__") and normalize-space(text())="{name}"]')
    
    @staticmethod
    def OFFLINE_CONVERSION_BY_NAME(name: str):
        return (By.XPATH, f'//div[@id="audience.offline_conversion"]//div[contains(@class, "EditableName_nameValue__") and normalize-space(text())="{name}"]')
    
    @staticmethod
    def AUDIENCE_BY_NAME(name: str):
        return (By.XPATH, f'//div[@id="audience"]//div[contains(@class, "NameCell_wrapper")]//h5[normalize-space(text())="{name}"]')
    
    AUDIENCE_SECTION = (By.XPATH, '//div[@id="tab_audience"]')
    USERLIST_SECTION = (By.XPATH, '//div[@id="tab_audience.users_list"]')
    OFFLINE_CONVERSION_SECTION = (By.XPATH, '//div[@id="tab_audience.offline_conversion"]')

    HINT = (By.XPATH, '//h5[contains(@class, "StatusCell_tooltipSubhead__")]')

    ADD_AUDIENCE_BUTTON = (By.XPATH, '//button[contains(.,"Создать аудиторию")]')
    ADD_LIST_BUTTON = (By.XPATH, '//button[contains(.,"Загрузить список")]')

    STATUS = (By.XPATH, '//div[@id="audience.users_list"]//div[contains(@class, "BaseTable__row")][1]//span[contains(@class, "StatusCell_label__")]')

    DELETE_BUTTON = (By.XPATH, '//label[@data-testid="dropdown-item" and contains(., "Удалить")]')
    DELETE_CONFIRM_BUTTON = (By.XPATH, '//div[contains(@class, "DeleteUsersListConfirm_buttons__")]//button[.//span[text()="Удалить"]]')
    MENU_BUTTON = (By.XPATH, '//div[@id="audience.users_list"]//div[contains(@class, "BaseTable__row")][1]//button[contains(@class, "ContextMenu_triggerButton__")]')
    AUDIENCE_MENU_BUTTON = (By.XPATH, '//div[@id="audience"]//div[contains(@class, "BaseTable__row")][1]//button[contains(@class, "ContextMenu_triggerButton__")]')
    DELETE_AUDIENCE_CONFIRM_BUTTON = (By.XPATH, '//div[contains(@class, "ModalConfirm_buttons__")]//button[.//span[text()="Удалить"]]')

    SUCCESS_MESSAGE = (By.XPATH, '//div[@id="Список успешно обновлен"]//div[contains(@class, "vkuiSnackbar__body")]')
    