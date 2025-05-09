from selenium.webdriver.remote.webelement import WebElement
import time

from ui.locators.registration_page_locators import RegistrationPageLocators
from .base_page import BasePage, PageNotOpenedException
from ui.pages.advertiser_sites_page import AdvertiserSites
import time



class Registration(BasePage):
    locators = RegistrationPageLocators
    url = 'https://ads.vk.com/hq/registration'

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()
        self.click(self.locators.SWITCH_MENU)
        self.click(self.locators.ACCOUNT)
        

    def go_to_advertiser_sites_page(self) -> AdvertiserSites:
        self.click(self.locators.SITES)
        return AdvertiserSites(self.driver)