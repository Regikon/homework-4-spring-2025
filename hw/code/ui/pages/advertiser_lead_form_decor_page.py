from dataclasses import dataclass
import os
import time
from ui.pages.advertiser_lead_form_question_page import LeadFormQuestionPage
from ui.locators.lead_form_page_locators import LeadFormDecorPageLocators
from ui.pages.base_page import BasePage

from ui.components.mediateka_component import MediaLoader

@dataclass
class CorrectDecorPageData:
    name: str
    logo: str
    company: str
    header: str
    description: str

class LeadFormDecorPage(BasePage):
    locators = LeadFormDecorPageLocators
    url = 'https://ads.vk.com/hq/leadads/leadforms'

    correct_page_data = correct_page_data = CorrectDecorPageData(
        name='Моя лид-форма',
        logo='./images/logo.jpg',
        company='Рога и копыта',
        header='Стулья',
        description='Продаём стулья'
    )

    @staticmethod
    def sale_locator_types():
        return {
            'price': LeadFormDecorPageLocators.BUTTON__SWITCH_RUBLE,
            'percent': LeadFormDecorPageLocators.BUTTON__SWITCH_PERCENT
        }

    def enter_lead_form_name(self, name):
        self.input_write(self.locators.INPUT__NAME, name)
    
    def enter_company_name(self, name):
        self.input_write(self.locators.INPUT__COMPANY, name)

    def enter_lead_form_header(self, header):
        self.input_write(self.locators.INPUT__HEADER, header)

    def enter_lead_form_description(self, description):
        self.input_write(self.locators.INPUT__DESCRIPTION, description)

    def set_up_logo(self, path):
        self.click(self.locators.INPUT__LOGO_UPLOAD)
        media_loader = MediaLoader(self.driver)
        media_loader.upload_image(path)
        filename = os.path.basename(path)
        print(filename)
        media_loader.select_image(filename)

    def set_up_cover(self, path):
        self.click(self.locators.INPUT__COVER_UPLOAD)
        media_loader = MediaLoader(self.driver)
        media_loader.upload_image(path)
        media_loader.select_image(os.path.basename(path))
    
    def switch_form_lead_magnet(self):
        self.click(self.locators.BUTTON__SELECT_LEAD_MAGNET)

    def enter_sale_size(self, type_locator, value):
        self.click(type_locator)
        self.input_write(self.locators.INPUT__SALE, value)
   
    def enter_bonus(self, value):
        self.switch_form_lead_magnet()
        self.click(self.locators.SWITCH__BONUS)
        self.input_write(self.locators.INPUT__BONUS, value)

    def click_continue(self):
        self.click(self.locators.BUTTON__CONTINUE)

    def go_to_questions_page(self, data: CorrectDecorPageData):
        self.enter_lead_form_name(data.name)
        self.enter_company_name(data.company)
        self.enter_lead_form_header(data.header)
        self.enter_lead_form_description(data.description)
        self.set_up_logo(data.logo)
        self.click_continue()
        return LeadFormQuestionPage(self.driver)  
