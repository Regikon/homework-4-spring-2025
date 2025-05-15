from selenium.webdriver.common.by import By

class AudienceAddOfflineConversionPageLocators:
    ADD_NEW_LIST_BUTTON = (By.XPATH, '//div[contains(@class, "vkuiCellButton ")][.//*[contains(., "Создать новый")]]')
    LIST_NAME_INPUT = (By.XPATH, '//input[@placeholder="Введите название списка"]')
    ADD_TO_EXISTING_LIST_BUTTON = (By.XPATH, '//div[contains(@class, "vkuiCellButton ")][.//*[contains(., "Добавить в существующий")]]')
    NAME_AS_FILE_CHECKBOX = (By.XPATH, '//label[contains(@class, "vkuiCheckbox")][.//*[contains(., "Как имя файла")]]')
    LIST_TYPE_DROPDOWN = (By.XPATH, '//div[contains(@class, "UploadListForm_listTypeSelect")]//input[@type="text"]')
    UPLOAD_FILE = (By.XPATH, '//label[contains(@class, "LocalFileSelector_file__")]//input[@type="file"]')
    SAVE_BUTTON = (By.XPATH, '//button[contains(.,"Сохранить")]')