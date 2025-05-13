from base_case import BaseCase, UserType
from ui.pages.advertiser_leadforms_page import LeadFormsPage

import pytest

class TestCreateLeadForms(BaseCase):
    user = UserType.ADVERTISER

    @pytest.fixture(scope="function")
    def decor_page(self, request):
        driver = self.driver
        driver.get(LeadFormsPage.url)
        return LeadFormsPage(driver).go_to_lead_forms_decor_page()

    @pytest.mark.skip('skip')
    def test_lead_form_name_long_error(self, decor_page):
        decor_page.enter_lead_form_name('a' * 256)
        assert decor_page.has_lead_form_name_long_error()

    @pytest.mark.skip('skip')
    def test_lead_form_name_empty_error(self, decor_page):
        decor_page.enter_lead_form_name('')
        assert decor_page.has_lead_form_name_empty_error()

    # def test_logo_empty_error(self, decor_page):
    #     decor_page.click_continue()
    #     assert decor_page.has_logo_empty_error()

    def test_logo_set_up(self, decor_page):
        decor_page.set_up_logo('./images/logo.jpg')
        assert decor_page.has_logo()
    
    # def 

