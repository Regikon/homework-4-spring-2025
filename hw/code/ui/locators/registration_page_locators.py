from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    SWITCH_MENU = (By.XPATH, '//div[contains(@class, "AccountSwitch_changeAccountButton__")]')
    ACCOUNT = (By.XPATH, '//div[@role="button" and contains(., "ID: 24817105")]')
    SITES = (By.XPATH, '//a[@href="/hq/pixels"]')