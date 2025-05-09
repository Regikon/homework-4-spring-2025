from selenium.webdriver.remote.webelement import WebElement

from ui.locators.pre_login_page_locators import PreLoginPageLocators
from ui.pages.id_auth_page import IdAuthPage
from .base_page import BasePage
#import allure

class PreLoginPage(BasePage):
    locators = PreLoginPageLocators
    url = 'https://ads.vk.com/'

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        self.is_opened()
        
    #@allure.step("Open login form")
    def go_to_login_page(self) -> IdAuthPage:
        self.click(self.locators.REGISTRATION_BUTTON)
        return IdAuthPage(self.driver)