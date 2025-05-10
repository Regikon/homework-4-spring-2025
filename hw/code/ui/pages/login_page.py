from ui.pages.base_page import BasePage
from ui.locators.login_page_locators import LoginPageLocators
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from ui.pages.undefined_profile_page import UndefinedProfilePage

class LoginPage(BasePage):
    url = 'https://id.vk.com/auth'
    locators = LoginPageLocators

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def login(self, timeout=60) -> UndefinedProfilePage:
        self.wait(timeout=timeout).until(EC.presence_of_element_located(self.locators.ACCOUNT))
        self.click(self.locators.ACCOUNT)
        return UndefinedProfilePage(self.driver)
