from ui.pages.base_page import BasePage
from ui.locators.audience_add_audience_page_locators import AudienceAddAudiencePageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

class AudienceAddAudiencePage(BasePage):
    url = 'https://ads.vk.com/hq/audience'
    locators = AudienceAddAudiencePageLocators

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def set_name(self, new_name: str):
        name_input = self.find(self.locators.AUDIENCE_NAME_INPUT)
        name_input.clear()
        name_input.send_keys(new_name)

    def add_source(self):
        add_source_button = self.find(self.locators.ADD_SOURCE_BUTTON)
        add_source_button.click()
        self.find(self.locators.AUDIENCE_SOURCE_BUTTON)

    def exclude_source(self):
        exclude_source_button = self.find(self.locators.EXCLUDE_SOURCE_BUTTON)
        exclude_source_button.click()
        self.find(self.locators.AUDIENCE_SOURCE_BUTTON)

    def choose_userlist_source(self):
        userlist_source_button = self.find(self.locators.USERLIST_SOURCE_BUTTON)
        userlist_source_button.click()
        self.find(self.locators.CREATE_NEW_LIST)

    def choose_events_from_announcements_source(self):
        events_from_announcements_source_button = self.find(self.locators.EVENTS_FROM_ANNOUNCEMENTS_SOURCE_BUTTON)
        events_from_announcements_source_button.click()

    def choose_audience_source(self):
        audience_source_button = self.find(self.locators.AUDIENCE_SOURCE_BUTTON)
        audience_source_button.click()

    def choose_mobile_categories_source(self):
        mobile_categories_source_button = self.find(self.locators.MOBILE_CATEGORIES_SOURCE_BUTTON)
        mobile_categories_source_button.click()

    def choose_events_from_lead_forms_source(self):
        events_from_lead_forms_source_button = self.find(self.locators.EVENTS_FROM_LEAD_FORMS_SOURCE_BUTTON)
        events_from_lead_forms_source_button.click()
    
    def choose_key_phrases_source(self):
        key_phrases_source_button = self.find(self.locators.KEY_PHRASES_SOURCE_BUTTON)
        key_phrases_source_button.click()

    def choose_community_subscribers_source(self):
        community_subscribers_source_button = self.find(self.locators.COMMUNITY_SUBSCRIBERS_SOURCE_BUTTON)
        community_subscribers_source_button.click()
        self.find(self.locators.ADD_BY_LIST_BUTTON)

    def choose_listeners_source(self):
        listeners_source_button = self.find(self.locators.LISTENERS_SOURCE_BUTTON)
        listeners_source_button.click()

    def choose_vk_mini_apps_source(self):
        self.wait_visibility(self.locators.VK_MINI_APPS_SOURCE_BUTTON)
        vk_mini_apps_source_button = self.find(self.locators.VK_MINI_APPS_SOURCE_BUTTON)
        vk_mini_apps_source_button.click()

    def create_new_list(self):
        self.wait_visibility(self.locators.CREATE_NEW_LIST)
        create_new_list_button = self.find(self.locators.CREATE_NEW_LIST)
        create_new_list_button.click()
    
    def wait_visibility(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_visibility_real(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

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

    def set_audience(self):
        list_dropdown = self.find(self.locators.AUDIENCE_TO_ADD_DROPDOWN)
        list_dropdown.click()
        self.find(self.locators.OPTION)
        list_dropdown.send_keys(Keys.ARROW_DOWN)
        list_dropdown.send_keys(Keys.RETURN)

    def click_save_button_in_modal(self):
        save_button = self.find(self.locators.SAVE_IN_MODAL_BUTTON)
        save_button.click()

    def click_save_button_in_modal_wait(self):
        save_button = self.find(self.locators.SAVE_IN_MODAL_BUTTON)
        save_button.click()
        self.wait_visibility_real(self.locators.OK_DIV)
        self.wait_invisibility(self.locators.OK_DIV)
    
    def wait_invisibility(self, locator, timeout=15):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))

    def add_key_phrase(self, key_phrases: str):
        key_phrases_input = self.find(self.locators.KEY_PHRASES_INPUT)
        key_phrases_input.clear()
        key_phrases_input.send_keys(key_phrases)
        ActionChains(self.driver).send_keys(Keys.TAB).perform()
        ActionChains(self.driver).send_keys(Keys.RETURN).perform()

    def add_communtity(self, community: str):
        self.wait_visibility(self.locators.ADD_BY_LIST_BUTTON)
        add_by_list_button = self.find(self.locators.ADD_BY_LIST_BUTTON)
        add_by_list_button.click()
        vk_communities_button = self.find(self.locators.VK_COMMUNITIES_BUTTON)
        vk_communities_button.click()
        textarea = self.find(self.locators.TEXTAREA)
        textarea.clear()
        textarea.send_keys(community)
        add_button = self.find(self.locators.ADD_BUTTON)
        add_button.click()
        close_modal = self.find(self.locators.CLOSE_MODAL)
        close_modal.click()
        self.find(self.locators.ADDED_COMMUNITY)

    def add_app(self, community: str):
        self.wait_visibility(self.locators.LOAD_BY_LIST_BUTTON)
        add_by_list_button = self.find(self.locators.LOAD_BY_LIST_BUTTON)
        add_by_list_button.click()
        textarea = self.find(self.locators.APPS_TEXTAREA)
        textarea.clear()
        textarea.send_keys(community)
        add_button = self.find(self.locators.ADD_BUTTON)
        add_button.click()
        close_modal = self.find(self.locators.CLOSE_MODAL)
        close_modal.click()

    def click_save_button(self):
        self.wait_visibility(self.locators.SAVE_BUTTON, timeout=15)
        save_button = self.find(self.locators.SAVE_BUTTON)
        save_button.click()
    
    def set_musician_name(self, musician_name: str):
        musician_name_input = self.find(self.locators.MUSICIAN_NAME_INPUT)
        musician_name_input.clear()
        musician_name_input.send_keys(musician_name)
        chosen_musician = self.find(self.locators.CHOSEN_MUSICIAN)
        chosen_musician.click()
        complete_button = self.find(self.locators.COMPLETE_BUTTON)
        complete_button.click()
        


    