import pytest
from base_case import BaseCase, UserType

from ui.locators.lead_form_settings_page import LeadFormSettingsPageLocators
from ui.pages.advertiser_leadforms_page import LeadFormsPage
from ui.pages.advertiser_lead_form_decor_page import LeadFormDecorPage, CorrectDecorPageData
from utils.random import generate_random_string

class TestCreateLeadFormSettingsPage(BaseCase):
    user = UserType.ADVERTISER

    @pytest.fixture(scope='function')
    def settings_page(self, request):
        driver = self.driver
        driver.get(LeadFormsPage.url)
        yield LeadFormsPage(driver).\
            go_to_lead_forms_decor_page().\
            go_to_questions_page(LeadFormDecorPage.correct_page_data).\
            go_to_result_page().\
            go_to_settings_page()
        lead_form_name = getattr(request.node, 'lead_form_name', None)
        if lead_form_name:
            LeadFormsPage(self.driver).remove_lead_form(lead_form_name)
    
    def test_enter_name_empty(self, settings_page):
        settings_page.enter_name('')
        assert settings_page.has_element(LeadFormSettingsPageLocators.NAME_EMPTY)

    def test_enter_address_empty(self, settings_page):
        settings_page.enter_address('')
        assert settings_page.has_element(LeadFormSettingsPageLocators.ADDRESS_EMPTY)
    
    def test_enter_inn_long(self, settings_page):
        settings_page.enter_inn('1' * 33)
        assert settings_page.has_element(LeadFormSettingsPageLocators.INN_LONG)

    def test_save_form(self, request, settings_page):
        lead_form_name = generate_random_string(10)
        request.node.lead_form_name = lead_form_name
        decor_page_data = CorrectDecorPageData(
            name=lead_form_name,
            logo='./images/logo.jpg',
            company='Рога и копыта',
            header='Стулья',
            description='Продаём стулья'
        )
        driver = self.driver
        driver.get(LeadFormsPage.url)
        settings_page =LeadFormsPage(driver).\
            go_to_lead_forms_decor_page().\
            go_to_questions_page(decor_page_data).\
            go_to_result_page().\
            go_to_settings_page()

        settings_page.enter_inn('123456789')
        settings_page.enter_name('Иван Иванов')
        settings_page.enter_address('Москва, ул. Пушкина, д. 1')
        assert settings_page.has_element(LeadFormsPage.locators.LEAD_FORM_NAME(lead_form_name))
        
        

