from typing import cast

from selenium.webdriver import ActionChains
from ui.locators.partner_site_ad_blocks_page_locators import PartnerSiteAdBlocksPageLocators
from ui.pages.ad_block_page import AdBlockPage
from ui.pages.add_ad_block_page import AddAdBlockPage
from ui.pages.base_page import BasePage
from ui.components.partner_site_header import PartnerSiteHeader
from utils.re_url import RegExpUrl
from ui.entities.ad_block_settings import AdBlockStatus

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

    def wait_to_block_to_disappear(self, id: int):
        self.wait_till_element_disappears(self.locators.BLOCK_ENTRY(id))

    def set_block_status(self, name: str, status: AdBlockStatus):
        self.select_block(name)
        locator = self.get_option_locator_by_status(status)
        self.open_actions_dropdown()
        self.click(locator)

    def select_block(self, name: str):
        checkbox = self.find(self.locators.BLOCK_CHECKBOX(name))
        if not checkbox.is_selected():
            checkbox.click()

    def search(self, query: str):
        input = self.find(self.locators.BLOCK_SEARCH_INPUT)
        ActionChains(self.driver).click(input).send_keys(query)

    def apply_filter(self, block_status: AdBlockStatus):
        if self.has_element(self.locators.CLEAR_ALL_BUTTON):
            self.click(self.locators.CLEAR_ALL_BUTTON)
        self.click(self.locators.FILTER_DROPDOWN)
        locator = self.get_filter_locator_by_status(block_status)
        self.click(locator)
        self.click(self.locators.APPLY_FILTER_BUTTON)


    def open_actions_dropdown(self):
        if self.has_element(self.locators.ARCHIVE_OPTION, 0.1):
            # already opened
            return
        self.click(self.locators.ACTIONS_DROPDOWN)

    def duplicate_block(self, block_id: int) -> AdBlockPage:
        duplicate_button = self.find(self.locators.DUPLICATE_BLOCK_BUTTON(block_id))
        ActionChains(self.driver).move_to_element(duplicate_button).click().perform()
        self.click(self.locators.CONFIRM_DUPLICATE_BUTTON)
        return AdBlockPage(self.driver)


    @classmethod
    def get_filter_locator_by_status(cls, status: AdBlockStatus):
        if status == AdBlockStatus.ARCHIVED:
            return cls.locators.ARCHIVED_FILTER
        if status == AdBlockStatus.STOPPED:
            return cls.locators.STOPPED_FILTER

    @classmethod
    def get_option_locator_by_status(cls , status: AdBlockStatus):
        if status == AdBlockStatus.ARCHIVED:
            return cls.locators.ARCHIVE_OPTION
        elif status == AdBlockStatus.STOPPED:
            return cls.locators.STOP_OPTION

    def get_block_status(self, block_id: int) -> AdBlockStatus:
        site_status_elem = self.find(self.locators.BLOCK_STATUS(block_id))
        status = site_status_elem.get_attribute('data-status')
        if status == "archived":
            return AdBlockStatus.ARCHIVED
        elif status == "stopped":
            return AdBlockStatus.STOPPED
        raise RuntimeError(f"Unknown status: {status}")
