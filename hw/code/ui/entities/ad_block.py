from selenium.webdriver.chrome.webdriver import WebDriver

from ui.pages.partner_site_ad_blocks_page import PartnerSiteAdBlocksPage
from ui.entities.ad_block_settings import AdBlockSettings, AdBlockStatus
from ui.pages.ad_block_page import AdBlockPage


class AdBlock(object):
    def __init__(self, site_id: int, settings: AdBlockSettings, driver: WebDriver) -> None:
        self.__settings = settings
        self.__site_id = site_id
        driver.get(PartnerSiteAdBlocksPage.generate_url(site_id))
        ad_blocks_page = PartnerSiteAdBlocksPage(driver)
        add_block_page = ad_blocks_page.go_to_add_block_page()
        add_block_page.fill_block_settings(self.__settings)
        block_page = add_block_page.submit()
        self.__id = block_page.block_id

    @property
    def site_id(self) -> int:
        return self.__site_id

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__settings['name']

    def remove(self, driver):
        driver.get(PartnerSiteAdBlocksPage.generate_url(self.__site_id))
        ad_blocks_page = PartnerSiteAdBlocksPage(driver)
        ad_blocks_page.set_block_status(self.name, AdBlockStatus.ARCHIVED)

    def go_to_block_page(self, driver: WebDriver) -> AdBlockPage:
        driver.get(AdBlockPage.generate_url(self.__site_id, self.__id))
        return AdBlockPage(driver)
