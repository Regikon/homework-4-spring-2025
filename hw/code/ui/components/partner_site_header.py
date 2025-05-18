from ui.components.base_component import BaseComponent
from ui.locators.partner_site_header_locators import PartnerSiteHeaderLocators

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class PartnerSiteHeader(BaseComponent):
    locators = PartnerSiteHeaderLocators

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    @property
    def site_name(self):
        return self.find(self.locators.SITE_NAME).text

    @property
    def site_link(self):
        return self.find(self.locators.SITE_LINK).text

    def set_site_name(self, name: str):
        site_name = self.find(self.locators.SITE_NAME)
        ActionChains(self.driver)\
            .click(site_name)\
            .send_keys(name)\
            .send_keys(Keys.RETURN)\
            .perform()
