from base_case import BaseCase, UserType
from ui.pages.advertiser_leadforms_page import LeadFormsPage

import pytest

class TestCreateLeadFormDecorPage(BaseCase):
    user = UserType.ADVERTISER

    @pytest.fixture(scope="function")
    def decor_page(self, request):
        driver = self.driver
        driver.get(LeadFormsPage.url)
        return LeadFormsPage(driver).go_to_lead_forms_decor_page()

    def test_lead_form_name_long_error(self, decor_page):
        decor_page.enter_lead_form_name('a' * 256)
        assert decor_page.has_lead_form_name_long_error()

    def test_lead_form_name_empty_error(self, decor_page):
        decor_page.enter_lead_form_name('')
        assert decor_page.has_lead_form_name_empty_error()

    def test_logo_empty_error(self, decor_page):
        decor_page.click_continue()
        assert decor_page.has_logo_empty_error()

    def test_logo_set_up(self, decor_page):
        decor_page.set_up_logo('./images/logo.jpg')
        assert decor_page.has_logo()
    
    def test_company_name_too_long_error(self, decor_page):
        decor_page.enter_company_name('a' * 31)
        assert decor_page.has_company_name_long_error()
    
    def test_company_name_empty_error(self, decor_page):
        decor_page.enter_company_name('')
        assert decor_page.has_company_name_empty_error()

    def test_header_too_long_error(self, decor_page):
        decor_page.enter_lead_form_header('a' * 51)
        assert decor_page.has_lead_form_header_long_error()
    
    def test_header_empty_error(self, decor_page):
        decor_page.enter_lead_form_header('')
        assert decor_page.has_lead_form_header_empty_error()

    def test_description_too_long_error(self, decor_page):
        decor_page.enter_lead_form_description('a' * 36)
        assert decor_page.has_lead_form_description_long_error()
    
    def test_description_empty_error(self, decor_page):
        decor_page.enter_lead_form_description('')
        assert decor_page.has_lead_form_description_empty_error()
    
    # @pytest.mark.skip('skip')
    def test_cover_set_up(self, decor_page):
        decor_page.set_up_cover('./images/cover.jpg')
        assert decor_page.has_cover()

    def test_lead_magnet_sale_zero_error(self, decor_page):
        decor_page.switch_form_lead_magnet()
        sale_type = decor_page.sale_locator_types()
        decor_page.enter_sale_size(sale_type['price'], '0')
        assert decor_page.has_lead_magnet_sale_zero_error()

    def test_lead_magnet_sale_bigger_100_percent(self, decor_page):
        decor_page.switch_form_lead_magnet()
        sale_type = decor_page.sale_locator_types()
        decor_page.enter_sale_size(sale_type['percent'], '101')
        assert decor_page.has_lead_magnet_sale_too_big()

    def test_lead_magnet_bonus_empty_error(self, decor_page):
        decor_page.enter_bonus('')
        assert decor_page.has_lead_magnet_bonus_empty_error()

    def test_lead_magnet_bonus_long_error(self, decor_page):
        decor_page.enter_bonus('a' * 31)
        assert decor_page.has_lead_magnet_bonus_long_error()

    # def test_go_to_questions_page(self, decor_page):
    #     decor_page.click_continue()
    #     assert decor_page.has_questions_page()
    
