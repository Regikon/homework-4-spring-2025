import time

from ui.locators import base_page_locators
from selenium.webdriver.chrome.webdriver import WebDriver

from ui.components.base_component import BaseComponent

class PageNotOpenedException(Exception):
    """
    PageNotOpenedException occures when the desired
    web page did not loaded in the webdriver
    """
    pass

class BasePage(BaseComponent):
    """
    BasePage is not actually a page but a group of a helper
    methods that are usable in the context of every page
    """

    locators = base_page_locators
    url = 'https://ads.vk.com'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.is_opened()

    def is_opened(self, timeout=15, starts_with_compare=False) -> bool:
        """
        Wait the page to be loaded. If it is not loaded in given timeout, throw PageNotOpenedException
        """
        started = time.time()
        while time.time() - started < timeout:
            if starts_with_compare and self.driver.current_url.startswith(self.url):
                return True
            elif not starts_with_compare and self.__trim_query(self.driver.current_url) == self.url:
                return True
        raise PageNotOpenedException(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __trim_query(self, url: str) -> str:
        query_start = url.find('?')
        if query_start > 0:
            return url[:query_start]
        return url
