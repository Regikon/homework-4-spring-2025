from ui.locators.partner_sites_page_locators import PartnerSitesPageLocators
from ui.pages.base_page import BasePage
from ui.pages.partner_add_site_page import PartnerAddSitePage
from selenium.webdriver.chrome.webdriver import WebDriver

class PartnerSitesPage(BasePage):
    url = 'https://ads.vk.com/h1/parner/sites'
    locators = PartnerSitesPageLocators

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def add_site(self) -> PartnerAddSitePage:
        self.click(self.locators.ADD_SITE_BUTTON)
        return PartnerAddSitePage(self.driver)

