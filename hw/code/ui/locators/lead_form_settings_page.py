from selenium.webdriver.common.by import By


class LeadFormSettingsPageLocators:
    ADDRESS = (By.XPATH, "//div[contains(@class, 'vkuiFormItem')][.//*[contains(., 'Адрес')]]//input")
    ADDRESS_EMPTY = (By.XPATH, "//div[contains(@class, 'vkuiFormItem')][.//*[contains(., 'Адрес')]]//*[contains(., 'Нужно заполнить')]")

    NAME = (By.XPATH, "//div[contains(@class, 'vkuiFormItem')][.//*[contains(., 'Фамилия')]]//input")
    NAME_EMPTY = (By.XPATH, "//div[contains(@class, 'vkuiFormItem')][.//*[contains(., 'Фамилия')]]//*[contains(., 'Нужно заполнить')]")

    INN = (By.XPATH, "//div[contains(@class, 'vkuiFormItem')][.//*[contains(., 'ИНН')]]//input")
    INN_LONG = (By.XPATH, "//div[contains(@class, 'vkuiFormItem')][.//*[contains(., 'ИНН')]]//*[contains(., 'Сократите')]")

    FORM = (By.XPATH, "//div[contains(@class, 'ModalRoot_componentWrapper')]")
