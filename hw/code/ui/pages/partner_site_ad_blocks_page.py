from ui.locators.partner_site_ad_blocks_page_locators import PartnerSiteAdBlocksPageLocators
from ui.pages.base_page import BasePage
from utils.re_url import RegExpUrl

from selenium.webdriver.chrome.webdriver import WebDriver


class PartnerSiteAdBlocksPage(BasePage):
    locators = PartnerSiteAdBlocksPageLocators
    url = RegExpUrl("https://ads.vk.com/hq/partner/sites/[0-9]+/blocks$")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @staticmethod
    def generate_url(site_id: int):
        return f"https://ads.vk.com/hq/partner/sites/{site_id}/blocks"
