from base_case import BaseCase, UserType
from ui.pages.partner_sites_page import PartnerSitesPage

import pytest

class TestAddPartnerSite(BaseCase):
    user = UserType.PARTNER

    @pytest.fixture(scope='function')
    def invalid_site_url(self) -> str:
        return '123123'

    def test_error_when_site_url_is_invalid(self, invalid_site_url: str):
        self.driver.get(PartnerSitesPage.url)
        add_site_page = PartnerSitesPage(self.driver).go_to_add_site_page()
        add_site_page.set_site_link(invalid_site_url)
        assert add_site_page.has_site_link_error()
