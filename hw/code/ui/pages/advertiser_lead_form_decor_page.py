from ui.locators.lead_form_page_locators import LeadFormDecorPageLocators
from ui.pages.base_page import BasePage

from ui.components.mediateka_component import MediaLoader

class LeadFormDecorPage(BasePage):
    locators = LeadFormDecorPageLocators
    url = 'https://ads.vk.com/hq/leadads/leadforms'

    def enter_lead_form_name(self, name):
        self.input_write(self.locators.INPUT__NAME, name)

    def has_lead_form_name_long_error(self):
        return self.find(self.locators.INPUT__NAME_ALERT_TOO_LONG) != None 
    
    def has_lead_form_name_empty_error(self):
        return self.find(self.locators.INPUT__NAME_ALERT_EMPTY) != None
    
    def enter_company_name(self, name):
        self.input_write(self.locators.INPUT__COMPANY, name)

    def enter_lead_form_header(self, header):
        self.input_write(self.locators.INPUT__HEADER, header)

    def enter_lead_form_description(self, description):
        self.input_write(self.locators.INPUT__DESCRIPTION, description)

    def switch_create_lending(self):
        pass

    def set_up_logo(self, path):
        self.click(self.locators.INPUT__LOGO_UPLOAD)
        media_loader = MediaLoader(self.driver)
        media_loader.upload_image(path)
        media_loader.select_image_cat()

    def has_logo(self):
        return self.find(self.locators.INPUT__LOGO_CHANGE) != None

    def has_logo_empty_error(self):
        return self.find(self.locators.INPUT__LOGO_EMPTY_ALERT) != None

    def click_continue(self):
        self.click(self.locators.BUTTON__CONTINUE)
