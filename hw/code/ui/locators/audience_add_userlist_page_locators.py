from selenium.webdriver.common.by import By

class AudienceAddUserlistPageLocators:
    ADD_NEW_USERLIST_BUTTON = (By.XPATH, '//div[contains(@class, "vkuiTabsItem")][.//*[contains(., "Создать новый")]]')
    ADD_TO_EXISTING_USERLIST_BUTTON = (By.XPATH, '//div[contains(@class, "vkuiTabsItem")][.//*[contains(., "Добавить в существующий")]]')
    EXCLUDE_FROM_USERLIST_BUTTON = (By.XPATH, '//div[contains(@class, "vkuiTabsItem")][.//*[contains(., "Исключить из существующего")]]')

    LIST_TO_ADD_DROPDOWN = (By.XPATH, '//div[contains(@class, "vkuiFormItem")][.//h5[text()="Список для добавления"]]//input')
    LIST_TO_EXCLUDE_DROPDOWN = (By.XPATH, '//div[contains(@class, "vkuiFormItem")][.//h5[text()="Список для исключения"]]//input')
    LIST_TYPE_DROPDOWN = (By.XPATH, '//div[contains(@class, "vkuiFormItem")][.//h5[text()="Тип списка"]]//input')
    
    LIST_NAME_INPUT = (By.XPATH, '//input[@placeholder="Введите название списка"]')
    SINGLE_LIST_OPTION = (By.XPATH, '//div[@id=":rc:-human"]/div[@class="vkuiCustomSelectOption__main"]/div[@class="vkuiCustomSelectOption__children"]')
    UPLOAD_FILE = (By.XPATH, '//label[contains(@class, "LocalFileSelector_file__")]//input[@type="file"]')
    NAME_AS_FILE_CHECKBOX = (By.XPATH, '//label[contains(@class, "vkuiCheckbox")][.//*[contains(., "Как имя файла")]]')
    ADD_NEW_AUDIENCE_CHECKBOX = (By.XPATH, '//label[contains(@class, "vkuiCheckbox")][.//*[contains(., "Создать новую аудиторию")]]')

    SAVE_BUTTON = (By.XPATH, '//button[contains(.,"Сохранить")]')

