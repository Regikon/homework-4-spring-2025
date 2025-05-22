from selenium.webdriver.common.by import By

class AudienceAddUserlistPageLocators: 
    @staticmethod
    def TAB_BY_LABEL(label_text: str):
        return (By.XPATH, f'//div[contains(@class, "vkuiTabsItem")][.//*[contains(text(), "{label_text}")]]')
    
    LIST_NAME_INPUT = (By.XPATH, '//input[@placeholder="Введите название списка"]')
    SINGLE_LIST_OPTION = (By.XPATH, '//div[@id=":rc:-human"]/div[@class="vkuiCustomSelectOption__main"]/div[@class="vkuiCustomSelectOption__children"]')
    UPLOAD_FILE = (By.XPATH, '//label[contains(@class, "LocalFileSelector_file__")]//input[@type="file"]')
    NAME_AS_FILE_CHECKBOX = (By.XPATH, '//label[contains(@class, "vkuiCheckbox")][.//*[contains(., "Как имя файла")]]')
    ADD_NEW_AUDIENCE_CHECKBOX = (By.XPATH, '//label[.//text()[contains(., "Создать новую аудиторию")]]')

    SAVE_BUTTON = (By.XPATH, '//button[contains(.,"Сохранить")]')
