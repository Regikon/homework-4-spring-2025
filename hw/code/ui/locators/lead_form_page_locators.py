from selenium.webdriver.common.by import By

class LeadFormPageLocators:
    BUTTON__CREATE_NEW = (By.XPATH, "//button[contains(., 'Создать лид-форму')]")
    INPUT__NAME = (By.XPATH, "//input[@placeholder='Название лид-формы']")
    INPUT__COMPANY = (By.XPATH, "//input[@placeholder='Название компании']")
    INPUT__HEADER = (By.XPATH, "//input[@placeholder='Название компании']")
    SWITCH__CREATE_LENDING = (By.CSS_SELECTOR, ".vkuiSwitch")
    BUTTON__EDIT_LENDING = (
        By.XPATH,
        "//*[contains(@class, 'vkuiButton__in') and contains(., 'Редактировать')]"
    )
    INPUT__LENDING_COMPANY = (By.XPATH, "//input[@placeholder='Введите название компании']")
    INPUT__LENDING_HEADER = (By.XPATH, "//textarea[@placeholder='Введите заголовок']")
    BUTTON__LENDING_ADD_BLOCK = (
        By.XPATH,
        "//*[contains(@class, 'vkuiButton__in') and contains(., 'Добавить блок')]"
    )
    BUTTON__LENDING_ADD_TEXT = (
        By.XPATH,
        "//*[contains(@class, 'AddBlockTooltip_option') and contains(., 'Текст')]"
    )
