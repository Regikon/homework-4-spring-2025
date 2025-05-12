from base_case import BaseCase, UserType
from ui.pages.partner_sites_page import PartnerSitesPage

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
            'name': 'uart.site'
        }

    def test_error_when_site_url_is_invalid(self, invalid_site_url: str):
        self.driver.get(PartnerSitesPage.url)
        add_site_page = PartnerSitesPage(self.driver).go_to_add_site_page()
        add_site_page.set_site_link(invalid_site_url)
        assert add_site_page.has_site_link_error()

    def test_error_when_site_name_is_empty(self, valid_site_params):
        self.driver.get(PartnerSitesPage.url)
        add_site_page = PartnerSitesPage(self.driver).go_to_add_site_page()
        add_site_page.set_site_link(valid_site_params['link'])
        add_site_page.set_site_name('')
        #TODO: assert add_site_page.has_empty_name_error()

    def test_error_when_site_name_is_too_large(self, valid_site_params):
        self.driver.get(PartnerSitesPage.url)
        add_site_page = PartnerSitesPage(self.driver).go_to_add_site_page()
        add_site_page.set_site_link(valid_site_params['link'])
        add_site_page.set_site_name('a' * (NAME_MAX_SYMBOLS_COUNT * 2))
        #TODO: assert add_site_page.has_too_large_name_error()

    def test_adds_valid_site(self, valid_site_params):
        self.driver.get(PartnerSitesPage.url)
        add_site_page = PartnerSitesPage(self.driver).go_to_add_site_page()
        ad_blocks_page = add_site_page.add_site(valid_site_params['link'], valid_site_params['name'])
        #TODO: get site id and go to sites page and assert that site is on page
