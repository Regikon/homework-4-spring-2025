from typing import cast
from ui.locators.partner_site_ad_blocks_page_locators import PartnerSiteAdBlocksPageLocators
from ui.pages.add_ad_block_page import AddAdBlockPage
from ui.pages.base_page import BasePage
from ui.components.partner_site_header import PartnerSiteHeader
from utils.re_url import RegExpUrl

from selenium.webdriver.chrome.webdriver import WebDriver
from parse import Result, parse


class PartnerSiteAdBlocksPage(BasePage):
    locators = PartnerSiteAdBlocksPageLocators
    url = RegExpUrl("https://ads.vk.com/hq/partner/sites/[0-9]+/blocks$")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        url = self.driver.current_url
        parsed_url = parse("https://ads.vk.com/hq/partner/sites/{site_id}/blocks", url)
        # safe since url is already validated
        self.__id = int(cast(Result, parsed_url).named['site_id'])
        self.header = PartnerSiteHeader(self.driver)

    @staticmethod
    def generate_url(site_id: int):
        return f"https://ads.vk.com/hq/partner/sites/{site_id}/blocks"

    @property
    def site_id(self) -> int:
        return self.__id

    def go_to_add_block_page(self) -> AddAdBlockPage:
        self.click(self.locators.ADD_AD_BLOCK_BUTTON)
        return AddAdBlockPage(self.driver)
