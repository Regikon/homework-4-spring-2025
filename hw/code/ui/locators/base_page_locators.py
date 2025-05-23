from selenium.webdriver.common.by import By

class BasePageLocators:
    @staticmethod
    def DROPDOWN_BY_LABEL(label_text: str):
        return (By.XPATH, f'//div[contains(@class, "vkuiFormItem")][.//*[contains(text(), "{label_text}")]]//input')
