from ui.components.base_component import BaseComponent
from ui.locators.partner_site_header_locators import PartnerSiteHeaderLocators

from selenium.webdriver.chrome.webdriver import WebDriver

class PartnerSiteHeader(BaseComponent):
    locators = PartnerSiteHeaderLocators

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    @property
    def site_name(self):
        return self.find(self.locators.SITE_NAME_INPUT).text

    @property
    def site_link(self):
        return self.find(self.locators.SITE_LINK).text

