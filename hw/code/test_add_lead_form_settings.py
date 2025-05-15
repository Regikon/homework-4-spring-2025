import time
import pytest
from base_case import BaseCase, UserType

from ui.pages.advertiser_leadforms_page import LeadFormsPage
from ui.pages.advertiser_lead_form_decor_page import LeadFormDecorPage

class TestCreateLeadFormSettingsPage(BaseCase):
    user = UserType.ADVERTISER

    @pytest.fixture(scope='function')
    def settings_page(self, request):
        driver = self.driver
        driver.get(LeadFormsPage.url)
        return LeadFormsPage(driver).\
            go_to_lead_forms_decor_page().\
            go_to_questions_page(LeadFormDecorPage.correct_page_data).\
            go_to_result_page().\
            go_to_settings_page()
    
    def test_enter_name_empty(self, settings_page):
        settings_page.enter_name('')
        assert settings_page.has_name_empty_error()

    def test_enter_address_empty(self, settings_page):
        settings_page.enter_address('')
        assert settings_page.has_address_empty_error()
    
    def test_enter_inn_long(self, settings_page):
        settings_page.enter_inn('1' * 33)
        assert settings_page.has_inn_long_error()

    def test_save_form(self, settings_page):
        settings_page.enter_inn('123456789')
        settings_page.enter_name('Иван Иванов')
        settings_page.enter_address('Москва, ул. Пушкина, д. 1')
        time.sleep(1)
        assert settings_page.is_modal_closed()

