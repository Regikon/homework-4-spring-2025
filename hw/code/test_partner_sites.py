
from typing import List
from selenium.webdriver.chrome.webdriver import WebDriver
from base_case import UserType, BaseCase
from ui.fixtures import get_default_driver
from ui.pages.partner_sites_page import PartnerSitesPage, SiteStatus
from utils.random import generate_random_string

import pytest


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

VALID_SITE_LINK = 'uart.site'

# I tried to make this class scoped fixture,
# but since driver is a function scoped fixture,
# we cannot have site with the same driver for
# all the test
@pytest.fixture(scope='function')
def two_sites():
    driver = get_default_driver()
    sites: List[PartnerSite] = []
    sites.append(PartnerSite.with_random_name(VALID_SITE_LINK, driver))
    sites.append(PartnerSite.with_random_name(VALID_SITE_LINK, driver))
    yield sites
    for site in sites:
        site.remove(driver)

@pytest.fixture(scope='function')
def one_site(driver):
    site = PartnerSite.with_random_name(VALID_SITE_LINK, driver)
    yield site
    site.remove(driver)

class TestPartnerSites(BaseCase):
    user = UserType.PARTNER

    def test_site_status_changes(self, one_site: PartnerSite):
        self.driver.get(PartnerSitesPage.url)
        sites_page = PartnerSitesPage(self.driver)
        sites_page.set_site_status(one_site.id, SiteStatus.STOPPED)
        self.driver.refresh()
        status = sites_page.get_site_status(one_site.id)
        assert status == SiteStatus.STOPPED
