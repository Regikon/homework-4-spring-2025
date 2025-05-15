from typing import List

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import POLL_FREQUENCY, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class BaseComponent(object):
    locators = None

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

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
        return self.driver.find_elements(by=locator[0], value=locator[1])

    def click(self, locator, timeout=None):
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def has_element(self, locator, timeout=None) -> bool:
        try:
            # if element is not found within the timeout, the exception will be thrown
            self.find(locator, timeout)
            return True
        except Exception:
            return False

    def wait_till_element_disappears(self, locator, timeout=5):
        started = time.time()
        while time.time() - started < timeout:
            if not self.has_element(locator, POLL_FREQUENCY):
                return True
        raise RuntimeError("Element still on the page")

