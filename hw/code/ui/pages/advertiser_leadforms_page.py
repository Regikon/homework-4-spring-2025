from ui.pages.base_page import BasePage
from ui.locators.lead_form_page_locators import LeadFormPageLocators
from ui.pages.advertiser_lead_form_decor_page import LeadFormDecorPage

class LeadFormsPage(BasePage):
    locators = LeadFormPageLocators
    url = 'https://ads.vk.com/hq/leadads/leadforms'

    def go_to_lead_forms_decor_page(self) -> LeadFormDecorPage:
        self.click(self.locators.BUTTON__CREATE_NEW)
        return LeadFormDecorPage(self.driver)
        