from ui.pages.base_page import BasePage
from ui.locators.audience_add_audience_page_locators import AudienceAddAudiencePageLocators
from selenium.webdriver.common.action_chains import ActionChains
import re

from selenium.webdriver.chrome.webdriver import WebDriver

class AudienceAddAudiencePage(BasePage):
    url = 'https://ads.vk.com/hq/audience'
    locators = AudienceAddAudiencePageLocators

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    