from selenium.webdriver.common.by import By

class AdBlockHeaderLocators:
    BLOCK_NAME = (By.XPATH, "//div[contains(concat(' ', normalize-space(@class), ' '), 'header_editableTextWrapper')]//*[contains(concat(' ', normalize-space(@class), ' '), 'EditableText_text')]")
    BLOCK_NAME_INPUT = (By.XPATH, "//div[contains(concat(' ', normalize-space(@class), ' '), 'EditableText_container_editing')]//input")
    BLOCK_FORMAT = (By.XPATH, '//div[contains(@class, "header_microWidget__")][contains(., "Формат")]//div[contains(@class, "header_description__")]')
    BLOCK_INTEGRATION = (By.XPATH, '//div[contains(@class, "header_microWidget__")][contains(., "Тип интеграции")]//div[contains(@class, "header_description__")]')
    GET_CODE_BUTTON = (By.XPATH, '//button[contains(text(), "Получить код")]')
    INTEGRATION_CODE = (By.XPATH, '//pre[contains(@class, "padIntegrationCodeModal_code__")]')
    COPY_INTEGRATION_CODE_BUTTON  = (By.XPATH, '//button[contains(., "Скопировать код")]')

    NAME_TOO_LONG_ERROR = (By.XPATH, "//*[contains(concat(' ', normalize-space(@class), ' '), 'header_editableTextError')][contains(., 'Название не должно превышать 200 символов')]")
