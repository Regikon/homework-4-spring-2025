from ui.components.ad_block_header import AdBlockHeader
from ui.pages.base_page import BasePage
from ui.locators.ad_block_page_locators import AdBlockPageLocators
from utils.re_url import RegExpUrl

from selenium.webdriver.chrome.webdriver import WebDriver
from parse import parse, Result
from typing import cast


class AdBlockPage(BasePage):
    locators = AdBlockPageLocators
    url = RegExpUrl("https://ads.vk.com/hq/partner/sites/[0-9]+/blocks/[0-9]+")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        url = self.driver.current_url
        parsed_url = parse("https://ads.vk.com/hq/partner/sites/{site_id}/blocks/{block_id}", url)
        self.__site_id = int(cast(Result, parsed_url).named['site_id'])
        self.__id = int(cast(Result, parsed_url).named['block_id'])
        self.header = AdBlockHeader(self.driver)

    @staticmethod
    def generate_url(site_id: int, block_id: int):
        return f"https://ads.vk.com/hq/partner/sites/{site_id}/blocks/{block_id}"

    @property
    def site_id(self) -> int:
        return self.__site_id

    @property
    def block_id(self) -> int:
        return self.__id
