import pytest
from base_case import BaseCase, UserType

from ui.pages.advertiser_leadforms_page import LeadFormsPage
from ui.pages.advertiser_lead_form_decor_page import LeadFormDecorPage
from ui.pages.advertiser_lead_form_result_page import LeadFormResultPage

class TestCreateLeadFormResultPage(BaseCase):
    user = UserType.ADVERTISER

    @pytest.fixture(scope='function')
    def result_page(self, request):
        driver = self.driver
        driver.get(LeadFormsPage.url)
        return LeadFormsPage(driver).\
            go_to_lead_forms_decor_page().\
            go_to_questions_page(LeadFormDecorPage.correct_page_data).\
            go_to_result_page()

    # bug with vk ads
    @pytest.mark.skip('skip')
    def test_heder_empty(self, result_page):
        result_page.enter_header('')
        assert result_page.has_enter_header_empty_error()

    def test_header_long(self, result_page):
        result_page.enter_header('a' * 26)
        assert result_page.has_enter_header_long_error()
    
    def test_description_long(self, result_page):
        result_page.enter_description('a' * 161)
        assert result_page.has_description_long_error()
    
    def test_add_site(self, result_page):
        result_page.click_add_site()
        result_page.enter_site('uart.site')
        assert result_page.has_site()

    def test_add_tel(self, result_page):
        result_page.click_add_tel()
        result_page.enter_tel('+7952812')
        assert result_page.has_tel()
        assert not result_page.has_tel_incorrect_error()

    def test_add_tel_incorrect(self, result_page):
        result_page.click_add_tel()
        result_page.enter_tel('123')
        assert result_page.has_tel_incorrect_error()
    
    def test_add_promo(self, result_page):
        result_page.click_add_promo()
        result_page.enter_promo('123')
        assert result_page.has_promo()
        assert not result_page.has_promo_too_long_error()

    def test_add_promo_too_long(self, result_page):
        result_page.click_add_promo()
        result_page.enter_promo('1' * 31)
        assert result_page.has_promo_too_long_error()
    

    
