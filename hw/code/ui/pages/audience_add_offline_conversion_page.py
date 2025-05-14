from ui.pages.base_page import BasePage
from ui.locators.audience_add_offline_conversion_page_locators import AudienceAddOfflineConversionPageLocators
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

class AudienceAddOfflineConversionPage(BasePage):
    url = 'https://ads.vk.com/hq/audience/offline_conversion'
    locators = AudienceAddOfflineConversionPageLocators

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def choose_add_to_existing_list(self):
        add_to_existing_list_button = self.find(self.locators.ADD_TO_EXISTING_LIST_BUTTON)
        add_to_existing_list_button.click()
        self.find(self.locators.LIST_TYPE_DROPDOWN)

    def choose_create_new_list(self):
        create_new_list_button = self.find(self.locators.ADD_NEW_LIST_BUTTON)
        create_new_list_button.click()
        self.find(self.locators.LIST_TYPE_DROPDOWN)

    def set_list_name(self, new_name: str):
        list_name_input = self.find(self.locators.LIST_NAME_INPUT)
        self.driver.execute_script("arguments[0].value = '';", list_name_input)
        list_name_input.send_keys(new_name)

    def set_list_type(self):
        list_type_dropdown = self.find(self.locators.LIST_TYPE_DROPDOWN)
        list_type_dropdown.click()
        list_type_dropdown.send_keys(Keys.ARROW_DOWN)
        list_type_dropdown.send_keys(Keys.RETURN)

    def upload_file(self, file_path: str):
        upload_file = self.find(self.locators.UPLOAD_FILE)
        upload_file.send_keys(file_path)

    def click_save_button(self):
        save_button = self.find(self.locators.SAVE_BUTTON)
        save_button.click()