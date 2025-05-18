import time
from ui.pages.base_page import BasePage
from ui.locators.lead_form_page_locators import LeadFormPageLocators
from ui.pages.advertiser_lead_form_decor_page import LeadFormDecorPage
from selenium.webdriver.common.action_chains import ActionChains

class LeadFormsPage(BasePage):
    locators = LeadFormPageLocators
    url = 'https://ads.vk.com/hq/leadads/leadforms'

    def go_to_lead_forms_decor_page(self) -> LeadFormDecorPage:
        self.click(self.locators.BUTTON__CREATE_NEW)
        return LeadFormDecorPage(self.driver)
    
    def remove_lead_form(self, lead_form_name: str) -> None:
        lead_form = self.find(self.locators.LEAD_FORM_NAME(lead_form_name))
        ActionChains(self.driver).\
            move_to_element(lead_form).\
            move_to_element(self.find(self.locators.REMOVE_BUTTON(lead_form_name))).\
            click().\
            perform()
        delete_button = self.find(self.locators.CONFIRM_DELETE_BUTTON)
        delete_button.click()
        