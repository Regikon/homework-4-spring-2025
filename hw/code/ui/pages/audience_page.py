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

    def click_button_add_userlist(self) -> AudienceAddUserlistPage:
        self.click(self.locators.ADD_LIST_BUTTON)
        return AudienceAddUserlistPage(self.driver)

    def go_to_add_userlist_page(self) -> AudienceAddUserlistPage:
        self.click(self.locators.USERLIST_SECTION)
        self.wait_clickability(self.locators.ADD_LIST_BUTTON)
        self.click(self.locators.ADD_LIST_BUTTON)
        return AudienceAddUserlistPage(self.driver)
    
    def go_to_add_offline_conversion_page(self) -> AudienceAddOfflineConversionPage:
        self.click(self.locators.OFFLINE_CONVERSION_SECTION)
        self.wait_clickability(self.locators.ADD_LIST_BUTTON)
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
    
    def open_status(self) -> float:
        status = self.find(self.locators.STATUS)
        ActionChains(self.driver).move_to_element(status).perform()
    
    def delete_userlist(self, name: str):
        if not self.has_element(self.locators.USERLIST_BY_NAME(name)):
            return
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
        if not self.has_element(self.locators.AUDIENCE_BY_NAME(name)):
            return
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