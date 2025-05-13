from ui.pages.base_page import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver
from ui.locators.advertiser_sites_page_locators import AdvertiserSitesLocators
from selenium.webdriver.common.action_chains import ActionChains
import time
from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class AdvertiserSitesPage(BasePage):
    locators = AdvertiserSitesLocators
    url = "https://ads.vk.com/hq/pixels"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def add_pixel(self, href):
        self.driver.set_window_size(2920, 1080)
        self.click(self.locators.ADD_PIXEL)
        self.find(self.locators.DOMAIN).send_keys(href)
        self.find_one_enabled(self.locators.ADD_PIXEL_IN_MODAL).click()
        
        self.click(self.locators.IGNORE_AND_CREATE_NEW)
        self.click(self.locators.DISMISS_BY_DOMAIN)
        return self.get_pixel_ID_by_href(href)
    
    def dell_pixel(self, href):
        self.more(href)
        time.sleep(1)
        self.click(self.locators.DELL_PIXEL_DROPDOWN)
        time.sleep(1)
        self.click(self.locators.DELETE_PIXEL)
        time.sleep(1)
        self.click(self.locators.CONFIRM_DELETE)

    def rename_pixel(self, href, new_name):
        self.more(href)
        self.click(self.locators.RENAME_PIXEL_DROPDOWN)
        self.find(self.locators.RENAME_INPUT).send_keys(new_name)
        self.click(self.locators.CONFIRM_RENAME)
    
    @staticmethod
    def PIXEL_ROW(href):
        return By.XPATH, f'//div[contains(@class, "PixelsList__row") and .//a[contains(@href, "{href}")]]'


    @staticmethod
    def SPAN_WITH_TEXT(name):
        return By.XPATH, f'//span[text()="{name}")] ]'


    def PIXEL_SETTINGS(self, href):
        print(self.get_pixel_ID_by_href(href))
        return By.XPATH, f'//a[text()="Настройка" and @data-route-param-id="{self.get_pixel_ID_by_href(href)}"]'

    @staticmethod
    def DROP_DOWN_CATEGORY(text):
        return By.XPATH, f'//div[@role="option" and text()="{text}"]'

    @staticmethod
    def SELECT_CATEGORY_FOR_EVENT(placeholder_text):
        return By.XPATH, '//input[@placeholder="{placeholder_text}"]'

    def hover(self, elem, timeout=5):
        pixel_row = self.find(elem)
        # Activate hover
        ActionChains(self.driver).move_to_element(pixel_row).perform()

    def more(self, href, timeout=5):
        print("hover")
        self.hover(self.PIXEL_ROW(href))
        # Wait for "More"
        print("not find")
        more_button = self.wait_visibility(self.locators.MORE_BUTTON)
        print("find")
        time.sleep(1)
        ActionChains(self.driver).move_to_element(more_button).click().perform()

    def get_pixel_ID_by_href(self, href):
        result = self.get_pixel_data()
        for row, site_href, pixel_id in result:
            if site_href == href:
                print("id: ", pixel_id)
                return pixel_id
        print("id not found")
        return None
    
    
    def get_pixel_data(self):
        result = []
        rows = self.find_all(self.locators.PIXEL_ROWS)
        for row in rows:
            try:
                site_elem = row.find_element(By.CSS_SELECTOR, 'a[href^="http"]')
                site_href = site_elem.get_attribute('href')

                id_elem = row.find_element(By.XPATH, './/div[contains(@class, "PixelIdCell_content")]')
                pixel_id = id_elem.text

                result.append([row, site_href, pixel_id])
            except Exception as e:
                print(f"Ошибка при разборе строки: {e}")
                continue
        return result

    def select_category(self, visible_text):
        self.click(self.locators.SELECT_CATEGORY_FOR_EVENT("Выберите категорию"))
        self.wait_visibility(self.DROP_DOWN_CATEGORY(visible_text)).click()

    def select_condition(self, visible_text):
        self.click(self.locators.SELECT_CATEGORY_FOR_EVENT("Выберите условие"))
        self.wait_visibility(self.DROP_DOWN_CATEGORY(visible_text)).click()

    
    def wait_visibility(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def find_one_enabled(self, locator):
        elements = self.find_all(locator)
        #print(elements)
        for element in elements:
            if element.is_displayed() and element.is_enabled():
                #print("found")
                return element
        return None
    
    def find_all(self, locator, timeout=None) -> List[WebElement]:
        self.wait(timeout).until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)
