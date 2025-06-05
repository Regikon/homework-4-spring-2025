import pytest
from base_case import BaseCase, UserType

from ui.locators.lead_form_questions_locators import LeadFormQuestionsLocators
from ui.pages.advertiser_leadforms_page import LeadFormsPage
from ui.pages.advertiser_lead_form_decor_page import LeadFormDecorPage

class TestCreateLeadFormQuestionPage(BaseCase):
    user = UserType.ADVERTISER

    QUESTION_TEXT = "Нужны стулья?"
    ANSWER_1_TEXT = "Да"
    ANSWER_2_TEXT = "Нет"
    ANSWER_3_TEXT = "Пропустить"
    CONTACT_NEW   = "Город"
    
    @pytest.fixture(scope='function')
    def question_page(self, request):
        driver = self.driver
        driver.get(LeadFormsPage.url)
        return LeadFormsPage(driver).\
            go_to_lead_forms_decor_page().\
            go_to_questions_page(LeadFormDecorPage.correct_page_data)
    
    def test_create_question(self, question_page):
        question_page.add_question()
        assert question_page.has_element(LeadFormQuestionsLocators.QUESTION_EXISTS)
        question_page.enter_question_text(self.QUESTION_TEXT)
        assert question_page.has_element(
            LeadFormQuestionsLocators.HAS_QUESTION_TEXT_ON_PREVIEW(self.QUESTION_TEXT)
        )
        question_page.add_answer_text(1, self.ANSWER_1_TEXT)
        question_page.add_answer_text(2, self.ANSWER_2_TEXT)
        assert question_page.has_element(
            LeadFormQuestionsLocators.HAS_ANSWER_ON_PREVIEW(self.ANSWER_1_TEXT)
        )
        assert question_page.has_element(
            LeadFormQuestionsLocators.HAS_ANSWER_ON_PREVIEW(self.ANSWER_2_TEXT)
        )

    def test_delete_question(self, question_page):
        question_page.add_question()
        assert question_page.has_element(LeadFormQuestionsLocators.QUESTION_EXISTS)
        question_page.remove_question()
        assert not question_page.has_element(LeadFormQuestionsLocators.QUESTION_EXISTS)

    def test_question_switch_type(self, question_page):
        question_page.add_question()
        assert question_page.has_element(LeadFormQuestionsLocators.QUESTION_EXISTS)
        question_page.switch_question_type_many_answers()
        assert question_page.has_element(LeadFormQuestionsLocators.HAS_QUESTION_TYPE_MANY_ANSWERS_ON_PREVIEW)

    def test_add_new_answer_in_question(self, question_page):
        question_page.add_question()
        assert question_page.has_element(LeadFormQuestionsLocators.QUESTION_EXISTS)
        question_page.add_answer_input()
        question_page.add_answer_text(3, self.ANSWER_3_TEXT)
        assert question_page.has_element(
            LeadFormQuestionsLocators.HAS_ANSWER_ON_PREVIEW(self.ANSWER_3_TEXT)
        )

    def test_add_contact_field_city(self, question_page):
        question_page.add_contact_field(self.CONTACT_NEW)
        assert question_page.has_element(LeadFormQuestionsLocators.HAS_CONTACTS_NAME_ON_PREVIEW)
        assert question_page.has_element(LeadFormQuestionsLocators.HAS_CONTACTS_TELEPHONE_ON_PREVIEW)
        assert question_page.has_element(LeadFormQuestionsLocators.HAS_CONTACTS_CITY_ON_PREVIEW)
        
