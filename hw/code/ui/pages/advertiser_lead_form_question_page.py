import pytest
from ui.pages.advertiser_lead_form_result_page import LeadFormResultPage
from ui.pages.base_page import BasePage
from ui.locators.lead_form_questions_locators import LeadFormQuestionsLocators


class LeadFormQuestionPage(BasePage):
    url = 'https://ads.vk.com/hq/leadads/leadforms'
    locators = LeadFormQuestionsLocators()

    def add_question(self):
        self.click(self.locators.ADD_QUESTION)
    
    def has_question(self):
        return self.has_element(self.locators.QUESTION_EXISTS)
    
    def enter_question_text(self, text):
        input = self.find(self.locators.QUESTION_TEXT)
        input.clear()
        input.send_keys(text)

    def has_question_text(self, text):
        return self.has_element(self.locators.HAS_QUESTION_TEXT_ON_PREVIEW(text))
    
    def add_answer_text(self, id: int, text: str):
        input = self.find(self.locators.ANSWER(id))
        input.clear()
        input.send_keys(text)
    
    def has_answer_text(self, text):
        return self.has_element(self.locators.HAS_ANSWER_ON_PREVIEW(text))
    
    def switch_question_type_many_answers(self):
        self.click(self.locators.QUESTION_TYPE)
        self.click(self.locators.QUESTION_TYPE_MANY_ANSWERS)

    def has_question_type_many_answers(self):
        return self.has_element(self.locators.HAS_QUESTION_TYPE_MANY_ANSWERS_ON_PREVIEW)
    
    def add_answer_input(self):
        self.click(self.locators.ADD_ANSWER)

    def remove_question(self):
        self.click(self.locators.REMOVE_QUESTION)

    def add_contact_field(self, text):
        self.click(self.locators.ADD_CONTACTS)
        self.click(self.locators.SELECT_CONTACT(text))
        self.click(self.locators.CONFIRM_CONTACTS)
    
    def has_contact_name_on_preview(self):
        return self.has_element(self.locators.HAS_CONTACTS_NAME_ON_PREVIEW)
    
    def has_contact_telephone_on_preview(self):
        return self.has_element(self.locators.HAS_CONTACTS_TELEPHONE_ON_PREVIEW)
    
    def has_contact_city_on_preview(self):
        return self.has_element(self.locators.HAS_CONTACTS_CITY_ON_PREVIEW)
    
    def go_to_result_page(self):
        self.click(self.locators.CONTINUE)
        return LeadFormResultPage(self.driver)
