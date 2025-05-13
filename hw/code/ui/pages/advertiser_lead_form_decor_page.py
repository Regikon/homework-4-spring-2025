from dataclasses import dataclass
import os
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

    @staticmethod
    def sale_locator_types():
        return {
            'price': LeadFormDecorPageLocators.BUTTON__SWITCH_RUBLE,
            'percent': LeadFormDecorPageLocators.BUTTON__SWITCH_PERCENT
        }

    def enter_lead_form_name(self, name):
        self.input_write(self.locators.INPUT__NAME, name)

    def has_lead_form_name_long_error(self):
        return self.has_element(self.locators.INPUT__NAME_ALERT_TOO_LONG)
    
    def has_lead_form_name_empty_error(self):
        return self.has_element(self.locators.INPUT__NAME_ALERT_EMPTY)
    
    def enter_company_name(self, name):
        self.input_write(self.locators.INPUT__COMPANY, name)

    def has_company_name_long_error(self):
        return self.has_element(self.locators.INPUT__COMPANY_ALERT_TOO_LONG)
    
    def has_company_name_empty_error(self):
        return self.has_element(self.locators.INPUT__COMPANY_ALERT_EMPTY)

    def enter_lead_form_header(self, header):
        self.input_write(self.locators.INPUT__HEADER, header)

    def has_lead_form_header_long_error(self):
        return self.has_element(self.locators.INPUT__HEADER_ALERT_TOO_LONG)
    
    def has_lead_form_header_empty_error(self):
        return self.has_element(self.locators.INPUT__HEADER_ALERT_EMPTY)

    def enter_lead_form_description(self, description):
        self.input_write(self.locators.INPUT__DESCRIPTION, description)

    def has_lead_form_description_long_error(self):
        return self.has_element(self.locators.INPUT__DESCRIPTION_ALERT_TOO_LONG)
    
    def has_lead_form_description_empty_error(self):
        return self.has_element(self.locators.INPUT__DESCRIPTION_ALERT_EMPTY)

    def switch_create_lending(self):
        pass

    def set_up_logo(self, path):
        self.click(self.locators.INPUT__LOGO_UPLOAD)
        media_loader = MediaLoader(self.driver)
        media_loader.upload_image(path)
        media_loader.select_image(os.path.basename(path))

    def has_logo(self):
        return self.has_element(self.locators.INPUT__LOGO_CHANGE)

    def has_logo_empty_error(self):
        return self.has_element(self.locators.INPUT__LOGO_EMPTY_ALERT)

    def set_up_cover(self, path):
        self.click(self.locators.INPUT__COVER_UPLOAD)
        media_loader = MediaLoader(self.driver)
        media_loader.upload_image(path)
        media_loader.select_image(os.path.basename(path))

    def has_cover(self):
        return self.has_element(self.locators.HAS_COVER)
    
    def switch_form_lead_magnet(self):
        self.click(self.locators.BUTTON__SELECT_LEAD_MAGNET)

    def enter_sale_size(self, type_locator, value):
        self.click(type_locator)
        self.input_write(self.locators.INPUT__SALE, value)
    
    def has_lead_magnet_sale_zero_error(self):
        return self.has_element(self.locators.INPUT__SALE_ALERT_ZERO)

    def has_lead_magnet_sale_too_big(self):
        return self.has_element(self.locators.INPUT__SALE_ALERT_TOO_BIG)
    
    def enter_bonus(self, value):
        self.switch_form_lead_magnet()
        self.click(self.locators.SWITCH__BONUS)
        self.input_write(self.locators.INPUT__BONUS, value)

    def has_lead_magnet_bonus_empty_error(self):
        return self.has_element(self.locators.INPUT__BONUS_ALERT_EMPTY)
    
    def has_lead_magnet_bonus_long_error(self):
        return self.has_element(self.locators.INPUT__BONUS_ALERT_TOO_LONG)

    def click_continue(self):
        self.click(self.locators.BUTTON__CONTINUE)

    def fill_correct_data(self):
        pass
