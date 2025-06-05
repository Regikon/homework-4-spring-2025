from ui.pages.base_page import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver
from ui.locators.advertiser_sites_page_locators import AdvertiserSitesLocators
from selenium.webdriver.common.action_chains import ActionChains
from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging

class AdvertiserSitesPage(BasePage):
    locators = AdvertiserSitesLocators
    url = "https://ads.vk.com/hq/pixels"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver.set_window_size(2620, 1080)

    def add_pixel(self, href):
        self.click(self.locators.ADD_PIXEL, timeout=20)
        self.find(self.locators.DOMAIN).send_keys(href)
        self.click(self.locators.ADD_PIXEL_IN_MODAL, timeout=10)
        self.click(self.locators.IGNORE_AND_CREATE_NEW)
        self.click(self.locators.DISMISS_BY_DOMAIN, timeout=10)
        return self.get_pixel_ID_by_href(href)
    
    def dell_pixel(self, href):
        self.more(href)
        self.click(self.locators.DELL_PIXEL_DROPDOWN)
        self.click(self.locators.CONFIRM_DELETE, timeout=40)
        self.wait_invisibility(self.locators.DELETE_PIXEL_H2, timeout=40)

    def rename_pixel(self, href, new_name):
        self.more(href)
        self.click(self.locators.RENAME_PIXEL_DROPDOWN)
        self.find(self.locators.RENAME_INPUT).send_keys(new_name)
        self.click(self.locators.CONFIRM_RENAME)
    
    @staticmethod
    def PIXEL_ROW(href):
        return By.XPATH, f'//div[contains(@class, "PixelsList__row") and .//a[contains(@href, "{href[:-1]}")]]'

    @staticmethod
    def DIV_WITH_TEXT(name):
        return By.XPATH, f'//div[text()="{name}"]'

    def PIXEL_SETTINGS(self, href):
        return By.XPATH, f'//a[text()="Настройка" and @data-route-param-id="{self.get_pixel_ID_by_href(href)}"]'

    @staticmethod
    def DROP_DOWN_CATEGORY(text):
        return By.XPATH, f'//div[@role="option" and text()="{text}"]'

    @staticmethod
    def SELECT_CATEGORY_FOR_EVENT(placeholder_text):
        return By.XPATH, '//input[@placeholder="{placeholder_text}"]'

    def hover(self, elem, timeout=5):
        pixel_row = self.find(elem)
        ActionChains(self.driver).move_to_element(pixel_row).perform()
        return pixel_row

    def more(self, href, timeout=5):
        self.sub_element(self.PIXEL_ROW(href), self.locators.MORE_BUTTON)

    def sub_element(self, elem, sub_elem, timeout=5):
        pixel_row = self.hover(elem)
        try:
            sub_element = WebDriverWait(self.driver, timeout).until(
                lambda d: pixel_row.find_element(*sub_elem)
            )
            WebDriverWait(self.driver, timeout).until(EC.visibility_of(sub_element))
            ActionChains(self.driver).move_to_element(sub_element).click().perform()
        except Exception as e:
            logging.error(f"Не удалось найти или кликнуть More: {e}")

    def get_pixel_ID_by_href(self, href):
        result = self.get_pixel_data()
        for row, site_href, pixel_id in result:
            if site_href == href:
                return pixel_id
        return None
    
    def get_pixel_data(self):
        result = []
        try:
            rows = self.find_all(self.locators.PIXEL_ROWS, timeout=10)
        except Exception:
            return []
        for row in rows:
            try:
                site_elem = row.find_element(By.CSS_SELECTOR, 'a[href^="http"]')
                site_href = site_elem.get_attribute('href')

                id_elem = row.find_element(By.XPATH, './/div[contains(@class, "PixelIdCell_content")]')
                pixel_id = id_elem.text

                result.append([row, site_href, pixel_id])
            except Exception as e:
                logging.error(f"Ошибка при разборе строки: {e}")
                continue
        return result

    def select_category(self):
        self.click(self.locators.INPUT_EVENT_CATEGORY)
        self.wait_clickability(self.locators.INPUT_CATEGORY).click()

    def select_condition(self):
        self.click(self.locators.INPUT_EVENT_CONDITION)
        self.wait_clickability(self.locators.INPUT_CONDITION).click()
    
    def wait_clickability(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_invisibility(self, locator, timeout=15):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))
    
    def wait_visibility(self, locator, timeout=15):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    
    def find_all(self, locator, timeout=None) -> List[WebElement]:
        self.wait(timeout).until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def reload(self):
        self.driver.refresh()

    def cancel_rename(self):
        self.click(self.locators.DISMISS_RENAME)

    def code_pixel_text_correct(self, text):
        self.click(self.locators.CODE_PIXEL_MENU)
        self.click(self.locators.DATA_LAYER_SWITCH)
        self.find(self.locators.DATA_LAYER_INPUT).send_keys(text)

    def create_event(self, event_name):
        self.click(self.locators.ADD_EVENT_TO_PIXEL)
        self.find(self.locators.INPUT_EVENT_NAME).send_keys(event_name)

    def url_contains(self, text_to_contain):
        self.find(self.locators.INPUT_URL_CONTAINS).send_keys(text_to_contain)

    def confirm_creating_event(self):
        self.click(self.locators.ADD_EVENT_TO_PIXEL_CONFIRM)

    def back_to_sites(self):
        self.click(self.locators.BACK_TO_SITES)
    
    def create_access(self, user_id):
        self.click(self.locators.ACCESS_PIXEL_MENU)
        self.click(self.locators.GIVE_ACCESS_BUTTON)
        self.find(self.locators.ACCESS_INPUT).send_keys(user_id)
        self.click(self.locators.ACCESS_GIVE_BUTTON)
        self.click(self.locators.ACCESS_CLOSE_BUTTON)

    def revoke_access(self):
        self.sub_element(self.locators.ACCESS_ROW, self.locators.REVOKE_ACCESS_BUTTON)
        self.click(self.locators.REVOKE_ACCESS_CONFIRM_BUTTON)

    def create_and_check_tag(self, tag_name):
        self.click(self.locators.TAGS_PIXEL_MENU)
        self.click(self.locators.CREATE_TAG_BUTTON)
        self.find(self.locators.TAG_INPUT).send_keys(tag_name)
        self.click(self.locators.TAG_INPUT_BUTTON)
        self.sub_element(self.locators.TAG_ROW, self.locators.SHOW_TAG_BUTTON)
        self.click(self.locators.TAG_CLOSE_BUTTON)