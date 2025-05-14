from ui.pages.base_page import BasePage
from ui.locators.audience_page_locators import AudiencePageLocators
from ui.pages.audience_add_userlist_page import AudienceAddUserlistPage
from selenium.webdriver.common.action_chains import ActionChains
import re
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver

class AudiencePage(BasePage):
    url = 'https://ads.vk.com/hq/audience'
    locators = AudiencePageLocators

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def go_to_add_userlist_page(self) -> AudienceAddUserlistPage:
        self.click(self.locators.USERLIST_SECTION)
        self.click(self.locators.ADD_LIST_BUTTON)
        return AudienceAddUserlistPage(self.driver)
    
    def go_to_userlist(self) -> AudienceAddUserlistPage:
        self.click(self.locators.USERLIST_SECTION)

    def has_userlist_with_name(self, name: str) -> bool:
        return self.has_element(self.locators.USERLIST_BY_NAME(name))
    
    def get_current_identifier(self) -> float:
        status = self.find(self.locators.STATUS)
        ActionChains(self.driver).move_to_element(status).perform()
        tooltip = self.find(self.locators.HINT)
        text = tooltip.text
        match = re.search(r'\d+', text)
        if not match:
            raise ValueError(f"Не удалось найти число в тексте подсказки: '{text}'")
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

    def has_success_message(self) -> bool:
        return self.has_element(self.locators.SUCCESS_MESSAGE)