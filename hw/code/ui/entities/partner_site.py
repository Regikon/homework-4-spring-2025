from ui.pages.add_ad_block_page import AddAdBlockPage
from ui.pages.partner_site_ad_blocks_page import PartnerSiteAdBlocksPage
from utils.random import generate_random_string
from selenium.webdriver.chrome.webdriver import WebDriver
from ui.pages.partner_sites_page import PartnerSitesPage, SiteStatus

class PartnerSite(object):
    """
    This class is responsible for keeping the state of partner site
    Driver is not keeped in the object
    """
    def __init__(self, link: str, name: str, driver: WebDriver) -> None:
        self.__link = link
        self.__name = name
        
        driver.get(PartnerSitesPage.url)
        add_site_page = PartnerSitesPage(driver).go_to_add_site_page()
        ad_blocks_page = add_site_page.add_site(self.__link, self.__name)
        self.__id = ad_blocks_page.site_id

    RANDOM_NAME_LEN = 10

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def link(self):
        return self.__link

    def remove(self, driver):
        driver.get(PartnerSitesPage.url)
        partner_sites_page = PartnerSitesPage(driver)
        partner_sites_page.set_site_status(self.__id, SiteStatus.ARCHIVED)

    @classmethod
    def with_random_name(cls, link: str, driver: WebDriver):
        return cls(link, generate_random_string(cls.RANDOM_NAME_LEN), driver)

    def go_to_site_page(self, driver: WebDriver) -> PartnerSiteAdBlocksPage:
        driver.get(PartnerSiteAdBlocksPage.generate_url(self.__id))
        return PartnerSiteAdBlocksPage(driver)

    def go_to_add_block_page(self, driver: WebDriver) -> AddAdBlockPage:
        ad_blocks_page = self.go_to_site_page(driver)
        return ad_blocks_page.go_to_add_block_page()

