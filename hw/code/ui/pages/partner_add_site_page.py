from typing import Optional
from ui.locators.partner_add_site_page_locators import PartnerAddSitePageLocators
from ui.pages.partner_site_ad_blocks_page import PartnerSiteAdBlocksPage
from ui.pages.base_page import BasePage

from selenium.webdriver.chrome.webdriver import WebDriver

class PartnerAddSitePage(BasePage):
    url = "https://ads.vk.com/hq/partner/sites"
    locators = PartnerAddSitePageLocators

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def set_site_link(self, new_link: str):
        site_link_input = self.find(self.locators.LINK_TO_THE_SITE_INPUT)
        site_link_input.clear()
        site_link_input.send_keys(new_link)

    def set_site_name(self, new_name: str):
        site_name_input = self.find(self.locators.SITE_NAME_INPUT)
        site_name_input.clear()
        site_name_input.send_keys(new_name)

    def add_site(self, link: str, name: Optional[str]) -> PartnerSiteAdBlocksPage:
        self.set_site_link(link)
        if name is not None:
            self.set_site_name(name)
        self.click(self.locators.ADD_SITE_BUTTON)
        return PartnerSiteAdBlocksPage(self.driver)

