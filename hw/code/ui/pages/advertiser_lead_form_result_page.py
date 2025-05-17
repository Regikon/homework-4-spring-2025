from ui.locators.lead_form_result_page_locators import LeadFormResultPageLocators
from ui.pages.base_page import BasePage
from ui.pages.advertiser_lead_form_settings import LeadFormSettingsPage


class LeadFormResultPage(BasePage):
    url = 'https://ads.vk.com/hq/leadads/leadforms'
    locators = LeadFormResultPageLocators

    def enter_header(self, header: str):
        self.input_write_without_submit(self.locators.HEADER, header)
        self.click(self.locators.CONTINUE)
   
    def enter_description(self, description: str):
        self.input_write_without_submit(self.locators.DESCRIPTION, description)
        self.click(self.locators.CONTINUE)

    def click_add_site(self):
        self.click(self.locators.ADD_SITE)
    
    def enter_site(self, link: str):
        self.input_write_without_submit(self.locators.SITE, link)

    def click_add_tel(self):
        self.click(self.locators.ADD_TEL)
    
    def enter_tel(self, tel: str):
        self.input_write_without_submit(self.locators.TEL, tel)
        self.click(self.locators.CONTINUE)

    def click_add_promo(self):
        self.click(self.locators.ADD_PROMO)
    
    def enter_promo(self, promo: str):
        self.input_write_without_submit(self.locators.PROMO, promo)
        self.click(self.locators.CONTINUE)
    
    def go_to_settings_page(self):
        self.click(self.locators.CONTINUE)
        return LeadFormSettingsPage(self.driver)
