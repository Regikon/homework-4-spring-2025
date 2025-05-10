from ui.pages.base_page import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver

class PartnerDashboardPage(BasePage):
    locators = None
    url = "https://ads.vk.com/hq/partner"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
