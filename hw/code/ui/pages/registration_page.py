from selenium.webdriver.remote.webelement import WebElement
import time

from ui.locators.registration_page_locators import RegistrationPageLocators
from .base_page import BasePage, PageNotOpenedException
from ui.pages.advertiser_sites_page import AdvertiserSites
import time



class Registration(BasePage):
    locators = RegistrationPageLocators
    url = 'https://ads.vk.com'

    def is_opened(self, timeout=15) -> bool:
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url.startswith(self.url):
                return True
        raise PageNotOpenedException(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def switch_account(self):
        self.click(self.locators.SWITCH_MENU)
        self.click(self.locators.ACCOUNT)
        

    def go_to_advertiser_sites_page(self) -> AdvertiserSites:
        self.click(self.locators.SITES)
        return AdvertiserSites(self.driver)