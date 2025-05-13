from base_case import BaseCase, UserType
from ui.pages.partner_sites_page import PartnerSitesPage
from selenium.webdriver.common.keys import Keys

import pytest

class TestAddPartnerSite(BaseCase):
    user = UserType.PARTNER

    NAME_MAX_SYMBOLS_COUNT = 200

    @pytest.fixture(scope='function')
    def invalid_site_url(self) -> str:
        return '123123'

    @pytest.fixture(scope='function')
    def valid_site_params(self) -> dict:
        return {
            'link': 'uart.site',
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
        add_site_page.set_site_name('a' * (self.NAME_MAX_SYMBOLS_COUNT * 2))
        assert add_site_page.has_too_large_name_error()
        assert not add_site_page.is_add_site_button_active()

    def test_adds_valid_site(self, valid_site_params):
        self.driver.get(PartnerSitesPage.url)
        add_site_page = PartnerSitesPage(self.driver).go_to_add_site_page()

        ad_blocks_page = add_site_page.add_site(valid_site_params['link'], valid_site_params['name'])

        site_id = ad_blocks_page.site_id
        assert ad_blocks_page.header.site_name == valid_site_params['name']
        assert ad_blocks_page.header.site_link == valid_site_params['link']
        self.driver.get(PartnerSitesPage.url)
        sites_page = PartnerSitesPage(self.driver)
        assert sites_page.has_site_with_id(site_id)
