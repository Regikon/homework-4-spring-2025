from selenium.webdriver.common.by import By


class UndefinedProfilePageLocators:
    SWITCH_PROFILE_DROPDOWN = (By.XPATH, '//div[contains(@class, "AccountSwitch_changeAccountButton")]')

    @staticmethod
    def ACCOUNT(id):
        return (By.XPATH, f'//div[@role="button" and contains(., "ID: {id}")]')
