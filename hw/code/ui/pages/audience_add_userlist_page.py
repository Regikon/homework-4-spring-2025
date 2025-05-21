from ui.pages.base_page import BasePage
from ui.locators.audience_add_userlist_page_locators import AudienceAddUserlistPageLocators
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AudienceAddUserlistPage(BasePage):
    url = 'https://ads.vk.com/hq/audience/user_lists'
    locators = AudienceAddUserlistPageLocators

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def set_list_name(self, new_name: str):
        list_name_input = self.find(self.locators.LIST_NAME_INPUT)
        self.driver.execute_script("arguments[0].value = '';", list_name_input)
        list_name_input.send_keys(new_name)

    def switch_to_add_to_existing_list(self):
        add_to_existing_list_button = self.find(self.locators.TAB_BY_LABEL('Добавить в существующий'))
        add_to_existing_list_button.click()
        self.find(self.locators.DROPDOWN_BY_LABEL('Список для добавления'))

    def switch_to_exclude_from_existing_list(self):
        exclude_from_existing_list_button = self.find(self.locators.TAB_BY_LABEL('Исключить из существующего'))
        exclude_from_existing_list_button.click()
        self.find(self.locators.DROPDOWN_BY_LABEL('Список для исключения'))

    def set_list_name_as_file(self):
        name_as_file_checkbox = self.find(self.locators.NAME_AS_FILE_CHECKBOX)
        name_as_file_checkbox.click()

    def set_list(self):
        list_dropdown = self.find(self.locators.DROPDOWN_BY_LABEL('Список для добавления'))
        list_dropdown.click()
        list_dropdown.send_keys(Keys.ARROW_DOWN)
        list_dropdown.send_keys(Keys.RETURN)

    def set_list_exclude(self):
        list_dropdown = self.find(self.locators.DROPDOWN_BY_LABEL('Список для исключения'))
        list_dropdown.click()
        list_dropdown.send_keys(Keys.ARROW_DOWN)
        list_dropdown.send_keys(Keys.RETURN)

    def upload_file(self, file_path: str):
        upload_file = self.find(self.locators.UPLOAD_FILE)
        upload_file.send_keys(file_path)

    def set_not_create_new_audience(self):
        create_new_audience_checkbox = self.find(self.locators.ADD_NEW_AUDIENCE_CHECKBOX)
        create_new_audience_checkbox.click()

    def click_save_button(self):
        save_button = self.find(self.locators.SAVE_BUTTON)
        save_button.click()
        self.wait_invisibility(self.locators.SAVE_BUTTON)
    
    def set_list_type(self):
        list_type_dropdown = self.find(self.locators.DROPDOWN_BY_LABEL('Тип списка'))
        list_type_dropdown.click()
        list_type_dropdown.send_keys(Keys.ARROW_DOWN)
        list_type_dropdown.send_keys(Keys.RETURN)

    def wait_invisibility(self, locator, timeout=15):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))