from ui.pages.base_page import BasePage
from ui.locators.main_page_locators import MainPageLocators
from selenium.webdriver.chrome.webdriver import WebDriver

from ui.pages.login_page import LoginPage

class MainPage(BasePage):
    url = 'https://ads.vk.com/'
    locators = MainPageLocators

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def go_to_login_page(self) -> LoginPage:
        self.click(self.locators.REGISTRATION_BUTTON)
        return LoginPage(self.driver)

