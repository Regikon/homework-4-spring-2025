import time
from typing import List

from selenium.webdriver.remote.webelement import WebElement

from ui.locators import base_page_locators
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageNotOpenedException(Exception):
    """
    PageNotOpenedException occures when the desired
    web page did not loaded in the webdriver
    """
    pass

class BasePage(object):
    """
    BasePage is not actually a page but a group of a helper
    methods that are usable in the context of every page
    """

    locators = base_page_locators
    url = 'https://ads.vk.com'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.is_opened()

    def is_opened(self, timeout=15, startswithcompare=False) -> bool:
        """
        Wait the page to be loaded. If it is not loaded in given timeout, throw PageNotOpenedException
        """
        started = time.time()
        while time.time() - started < timeout:
            if startswithcompare and self.driver.current_url.startswith(self.url):
                return True
            elif not startswithcompare and self.__trim_query(self.driver.current_url) == self.url:
                return True
        raise PageNotOpenedException(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def wait(self, timeout=None) -> WebDriverWait:
        """
        Get WebDriverWait object with given timeout
        """
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None) -> WebElement:
        """
        Find the element by locator. Waits for the element to be loaded with given timeout
        """
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def find_all(self, locator, timeout=None) -> List[WebElement]:
        self.wait(timeout).until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(locator)

    def click(self, locator, timeout=None):
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def __trim_query(self, url: str) -> str:
        query_start = url.find('?')
        if query_start > 0:
            return url[:query_start]
        return url
