from ui.pages.base_page import BasePage
from ui.locators.audience_add_offline_conversion_page_locators import AudienceAddOfflineConversionPageLocators
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

class AudienceAddOfflineConversionPage(BasePage):
    url = 'https://ads.vk.com/hq/audience/offline_conversion'
    locators = AudienceAddOfflineConversionPageLocators

    def __init__(self, driver: WebDriver):
        super().__init__(driver)