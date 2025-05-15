from selenium.webdriver.common.by import By


class AddAdBlockPageLocators:
    SITE_IS_AMP_PAGE_CHECKBOX = (By.XPATH, "//input[@name='isAmp']/..")
    AD_BLOCK_NAME_INPUT = (By.XPATH, '//input[@placeholder="Название блока"]')
    NAME_ERROR = (By.XPATH, '//*[contains(., "Название рекламного блока")]//span[@role="alert"]')

    DISPLAY_BLOCK_OPTION = (By.XPATH, '//*[@data-value="banner"]')
    AMP_DISPLAY_BLOCK_OPTION = (By.XPATH, '//*[@data-value="amp"]')
    RECOMMEND_WIDGET_OPTION = (By.XPATH, '//*[@data-value="recomend"]')
    INSTREAM_VIDEO_OPTION = (By.XPATH, '//*[@data-value="instream]')

    @staticmethod
    def BLOCK_SIZE_OPTION(size: str):
        return (By.XPATH, f'//*[@data-format_options-ui-format_name="{size}"]')

    SIZE_SELECTION_RADIOGROUP = (By.XPATH, '//*[contains(@class, "SizeSelect_root")]')

    DESIGN_SETTINGS_BUTTON = (By.XPATH, '//button[contains(., "Настроить дизайн")]')

    DIRECT_INTEGRATION_RADIOBUTTON = (By.XPATH, '//input[@value="js_sdk"]/..')
    HEADER_BIDDING_INTEGRATION_RADIOBUTTON = (By.XPATH, '//input[@value="header_bidding"]/..')

    AUTO_CPM_RADIOBUTTON = (By.XPATH, '//input[@value="auto"]/..')
    MANUAL_CPM_RADIOBUTTON = (By.XPATH, '//input[@value="manual"]/..')

    CALL_CODE_TEXTAREA = (By.XPATH, '//textarea[@placeholder="Введите код вызова"]')

    SHOW_LIMIT_SELECT = (By.XPATH, '//div[contains(@class, "vkuiFormItem")][contains(., "Лимит показов")]//input')
    SHOW_PERIOD_SELECT = (By.XPATH, '//div[contains(@class, "vkuiFormItem")][contains(., "за период")]//input')
    SHOW_INTERVAL_SELECT = (By.XPATH, '//div[contains(@class, "vkuiFormItem")][contains(., "Интервал")]//input')
    @staticmethod
    def SELECT_OPTION(id: str):
        return (By.XPATH, f'//*[@role="option"][contains(@id, {id})]')

    SUBMIT_BUTTON = (By.XPATH, '//button[@data-testid="submit"]')

    SITE_SELECT = (By.XPATH, '//div[contains(@class, "vkuiFormItem")][contains(., "Сайт")]//*[contains(@class, "CreatePadForm_input")]')

    @staticmethod
    def SITE_OPTION(site_id: int):
        return (By.XPATH, f"//div[contains(@id, '{site_id}')]")
