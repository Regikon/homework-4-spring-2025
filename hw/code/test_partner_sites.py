
from typing import List
from selenium.webdriver import Keys
from base_case import UserType, BaseCase
from ui.pages.partner_sites_page import PartnerSitesPage, SiteStatus
from ui.entities.partner_site import PartnerSite

import pytest


VALID_SITE_NAME_MAX_SYMBOLS_COUNT = 200
VALID_SITE_LINK = "uart.site"

class TestAddPartnerSite(BaseCase):
    user = UserType.PARTNER


    @pytest.fixture(scope='function')
    def invalid_site_url(self) -> str:
        return '123123'

    @pytest.fixture(scope='function')
    def valid_site_params(self) -> dict:
        return {
            'link': VALID_SITE_LINK,
            'name': 'uart'
        }

    def test_error_when_site_url_is_invalid(self, invalid_site_url: str):
        self.driver.get(PartnerSitesPage.url)
        add_site_page = PartnerSitesPage(self.driver).go_to_add_site_page()
        add_site_page.set_site_link(invalid_site_url)
        assert add_site_page.has_site_link_error()
        assert not add_site_page.is_add_site_button_active()

    def test_error_when_site_name_is_empty(self, valid_site_params):
        self.driver.get(PartnerSitesPage.url)
        add_site_page = PartnerSitesPage(self.driver).go_to_add_site_page()
        add_site_page.set_site_link(valid_site_params['link'])
        add_site_page.set_site_name('a' + Keys.BACKSPACE)
        assert add_site_page.has_empty_name_error()
        assert not add_site_page.is_add_site_button_active()

    def test_error_when_site_name_is_too_large(self, valid_site_params):
        self.driver.get(PartnerSitesPage.url)
        add_site_page = PartnerSitesPage(self.driver).go_to_add_site_page()
        add_site_page.set_site_link(valid_site_params['link'])
        add_site_page.set_site_name('a' * (VALID_SITE_NAME_MAX_SYMBOLS_COUNT * 2))
        assert add_site_page.has_too_large_name_error()
        assert not add_site_page.is_add_site_button_active()

    def test_adds_valid_site(self, valid_site_params):
        # We manually adding the site without PartnerSite class
        # In order to gain more options to make asserts
        self.driver.get(PartnerSitesPage.url)
        add_site_page = PartnerSitesPage(self.driver).go_to_add_site_page()

        ad_blocks_page = add_site_page.add_site(valid_site_params['link'], valid_site_params['name'])

        site_id = ad_blocks_page.site_id
        assert ad_blocks_page.header.site_name == valid_site_params['name']
        assert ad_blocks_page.header.site_link == valid_site_params['link']
        self.driver.get(PartnerSitesPage.url)
        sites_page = PartnerSitesPage(self.driver)
        assert sites_page.has_site_with_id(site_id)

class TestPartnerSite(BaseCase):
    user = UserType.PARTNER

    VALID_SITE_NAME = 'best-page'

    def test_site_changes_name(self, one_site: PartnerSite):
        site_page = one_site.go_to_site_page(self.driver)
        site_page.header.set_site_name(self.VALID_SITE_NAME)
        self.driver.refresh()
        assert site_page.header.site_name == self.VALID_SITE_NAME

    def test_site_cannot_change_to_empty_name(self, one_site: PartnerSite):
        site_page = one_site.go_to_site_page(self.driver)
        site_page.header.set_site_name('a' + Keys.BACKSPACE)
        assert site_page.header.is_name_input_active()

    def test_error_if_try_to_set_too_long_site_name(self, one_site: PartnerSite):
        site_page = one_site.go_to_site_page(self.driver)
        site_page.header.set_site_name('a' * (2 * VALID_SITE_NAME_MAX_SYMBOLS_COUNT))
        assert site_page.header.has_name_too_long_error()

class TestPartnerSites(BaseCase):
    user = UserType.PARTNER

    UNEXISTANT_SITE_NAME = "opvhizpsconva[sdjkfqawejr;jasd;ljv;lscjkl]"

    def test_site_status_changes(self, one_site: PartnerSite):
        self.driver.get(PartnerSitesPage.url)
        sites_page = PartnerSitesPage(self.driver)
        sites_page.set_site_status(one_site.id, SiteStatus.STOPPED)
        self.driver.refresh()
        status = sites_page.get_site_status(one_site.id)
        assert status == SiteStatus.STOPPED

    def test_site_list_filters_stopped_sites(self, two_sites: List[PartnerSite]):
        self.driver.get(PartnerSitesPage.url)
        sites_page = PartnerSitesPage(self.driver)
        first_site = two_sites[0]
        second_site = two_sites[1]
        sites_page.set_site_status(first_site.id, SiteStatus.STOPPED)
        sites_page.apply_filter(SiteStatus.STOPPED)
        assert sites_page.has_site_with_id(first_site.id)
        assert not sites_page.has_site_with_id(second_site.id)
        assert sites_page.does_not_have_archived_sites()

    def test_site_search_finds_site(self, two_sites: List[PartnerSite]):
        self.driver.get(PartnerSitesPage.url)
        sites_page = PartnerSitesPage(self.driver)
        first_site = two_sites[0]
        second_site = two_sites[1]
        sites_page.search(first_site.name)
        assert sites_page.has_site_with_id(first_site.id)
        assert not sites_page.has_site_with_id(second_site.id)

    def test_site_shows_nothing_found_if_nothing_found(self):
        self.driver.get(PartnerSitesPage.url)
        sites_page = PartnerSitesPage(self.driver)
        sites_page.search(self.UNEXISTANT_SITE_NAME)
        assert sites_page.has_nothing_found_caption()
