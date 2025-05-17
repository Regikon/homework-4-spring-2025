import pytest
from ui.pages.advertiser_lead_form_result_page import LeadFormResultPage
from ui.pages.base_page import BasePage
from ui.locators.lead_form_questions_locators import LeadFormQuestionsLocators


class LeadFormQuestionPage(BasePage):
    url = 'https://ads.vk.com/hq/leadads/leadforms'
    locators = LeadFormQuestionsLocators()

    def add_question(self):
        self.click(self.locators.ADD_QUESTION)
    
    def enter_question_text(self, text):
        input = self.find(self.locators.QUESTION_TEXT)
        input.clear()
        input.send_keys(text)
    
    def add_answer_text(self, id: int, text: str):
        input = self.find(self.locators.ANSWER(id))
        input.clear()
        input.send_keys(text)
    
    def switch_question_type_many_answers(self):
        self.click(self.locators.QUESTION_TYPE)
        self.click(self.locators.QUESTION_TYPE_MANY_ANSWERS)
    
    def add_answer_input(self):
        self.click(self.locators.ADD_ANSWER)

    def remove_question(self):
        self.click(self.locators.REMOVE_QUESTION)

    def add_contact_field(self, text):
        self.click(self.locators.ADD_CONTACTS)
        self.click(self.locators.SELECT_CONTACT(text))
        self.click(self.locators.CONFIRM_CONTACTS)
    
    def go_to_result_page(self):
        self.click(self.locators.CONTINUE)
        return LeadFormResultPage(self.driver)
