from ui.pages.base_page import BasePage
from ui.locators.lead_form_page_locators import LeadFormPageLocators

class LeadFormsPage(BasePage):
    locators = LeadFormPageLocators
    url = 'https://ads.vk.com/hq/leadads/leadforms'

    def create_new_lead_form(self):
        self.click(self.locators.BUTTON__CREATE_NEW)
    
    def enter_lead_form_name(self, name):
        self.input_write(self.locators.INPUT__NAME, name)

    def enter_company_name(self, name):
        self.input_write(self.locators.INPUT__COMPANY, name)

    def enter_lead_form_header(self, header):
        self.input_write(self.locators.INPUT__HEADER, header)

    def enter_lead_form_description(self, description):
        self.input_write(self.locators.INPUT__DESCRIPTION, description)

    def switch_create_lending(self):
        pass

    

