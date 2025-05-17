from ui.locators.lead_form_settings_page import LeadFormSettingsPageLocators
from ui.pages.base_page import BasePage


class LeadFormSettingsPage(BasePage):
    url = 'https://ads.vk.com/hq/leadads/leadforms'
    locators = LeadFormSettingsPageLocators

    def enter_name(self, name):
        self.input_write(self.locators.NAME, name)

    def enter_address(self, address):
        self.input_write(self.locators.ADDRESS, address)

    def enter_inn(self, inn):
        self.input_write(self.locators.INN, inn)
