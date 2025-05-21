from ui.pages.base_page import BasePage
from ui.locators.audience_page_locators import AudiencePageLocators
from ui.pages.audience_add_userlist_page import AudienceAddUserlistPage
from ui.pages.audience_add_audience_page import AudienceAddAudiencePage
from ui.pages.audience_add_offline_conversion_page import AudienceAddOfflineConversionPage
from selenium.webdriver.common.action_chains import ActionChains
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.webdriver import WebDriver

class AudiencePage(BasePage):
    url = 'https://ads.vk.com/hq/audience' 
    locators = AudiencePageLocators

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def add_userlist(self) -> AudienceAddUserlistPage:
        self.click(self.locators.ADD_LIST_BUTTON)
        return AudienceAddUserlistPage(self.driver)

    def go_to_add_userlist_page(self) -> AudienceAddUserlistPage:
        self.click(self.locators.USERLIST_SECTION)
        self.wait_visibility(self.locators.ADD_LIST_BUTTON)
        self.click(self.locators.ADD_LIST_BUTTON)
        return AudienceAddUserlistPage(self.driver)
    
    def go_to_add_offline_conversion_page(self) -> AudienceAddOfflineConversionPage:
        self.click(self.locators.OFFLINE_CONVERSION_SECTION)
        self.wait_visibility(self.locators.ADD_LIST_BUTTON)
        self.click(self.locators.ADD_LIST_BUTTON)
        return AudienceAddOfflineConversionPage(self.driver)
    
    def go_to_audience_page(self):
        self.click(self.locators.AUDIENCE_SECTION)
    
    def go_to_add_audience_page(self) -> AudienceAddAudiencePage:
        self.click(self.locators.ADD_AUDIENCE_BUTTON)
        return AudienceAddAudiencePage(self.driver)

    def reload(self):
        ActionChains(self.driver).send_keys(Keys.F5).perform()
    
    def go_to_userlist(self) -> AudienceAddUserlistPage:
        self.click(self.locators.USERLIST_SECTION)
    
    def get_current_identifier(self) -> float:
        status = self.find(self.locators.STATUS)
        ActionChains(self.driver).move_to_element(status).perform()
        tooltip = self.find(self.locators.HINT)
        text = tooltip.text
        match = re.search(r'\d+', text)
        return float(match.group())
    
    def delete_userlist(self, name: str):
        userlist = self.find(self.locators.USERLIST_BY_NAME(name))
        ActionChains(self.driver).move_to_element(userlist).perform()
        menu = self.find(self.locators.MENU_BUTTON)
        ActionChains(self.driver).move_to_element(menu).click(menu).perform()
        delete_button = self.find(self.locators.DELETE_BUTTON)
        delete_button.click()
        delete_confirm_button = self.find(self.locators.DELETE_CONFIRM_BUTTON)
        delete_confirm_button.click()
        self.wait_invisibility(self.locators.DELETE_CONFIRM_BUTTON)

    def delete_audience(self, name: str):
        userlist = self.find(self.locators.AUDIENCE_BY_NAME(name))
        ActionChains(self.driver).move_to_element(userlist).perform()
        menu = self.find(self.locators.AUDIENCE_MENU_BUTTON)
        ActionChains(self.driver).move_to_element(menu).click(menu).perform()
        delete_button = self.find(self.locators.DELETE_BUTTON)
        delete_button.click()
        delete_confirm_button = self.find(self.locators.DELETE_AUDIENCE_CONFIRM_BUTTON)
        delete_confirm_button.click()
        self.wait_invisibility(self.locators.DELETE_AUDIENCE_CONFIRM_BUTTON)

    def has_success_message(self) -> bool:
        return self.has_element(self.locators.SUCCESS_MESSAGE)
    
    def wait_invisibility(self, locator, timeout=15):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))
    
    def wait_visibility(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))