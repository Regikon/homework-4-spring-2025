from ui.locators.lead_form_settings_page import LeadFormSettingsPageLocators
from ui.pages.base_page import BasePage


class LeadFormSettingsPage(BasePage):
    url = 'https://ads.vk.com/hq/leadads/leadforms'
    locators = LeadFormSettingsPageLocators

    def enter_name(self, name):
        self.input_write(self.locators.NAME, name)

    def has_name_empty_error(self):
        return self.has_element(self.locators.NAME_EMPTY)
    
    def enter_address(self, address):
        self.input_write(self.locators.ADDRESS, address)

    def has_address_empty_error(self):
        return self.has_element(self.locators.ADDRESS_EMPTY)

    def enter_inn(self, inn):
        self.input_write(self.locators.INN, inn)

    def has_inn_long_error(self):
        return self.has_element(self.locators.INN_LONG)
    
    def is_modal_closed(self):
        return not self.has_element(self.locators.FORM)
