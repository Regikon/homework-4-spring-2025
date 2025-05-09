from selenium.webdriver.remote.webelement import WebElement
import time

from ui.locators.id_auth_page_locators import IdAuthPageLocators
from .base_page import BasePage, PageNotOpenedException
from ui.pages.registration_page import Registration



class IdAuthPage(BasePage):
    locators = IdAuthPageLocators
    url = 'https://id.vk.com/'

    def is_opened(self, timeout=15) -> bool:
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url.startswith(self.url):
                return True
        raise PageNotOpenedException(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def go_to_registration_page(self) -> Registration:
        self.click(self.locators.ACCOUNT)
        return Registration(self.driver)