from ui.pages.base_page import BasePage
from ui.locators.audience_add_audience_page_locators import AudienceAddAudiencePageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
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
        self.find(self.locators.SOURCE_BUTTON_BY_LABEL('Уже созданная аудитория'))

    def exclude_source(self):
        exclude_source_button = self.find(self.locators.EXCLUDE_SOURCE_BUTTON)
        exclude_source_button.click()
        self.find(self.locators.SOURCE_BUTTON_BY_LABEL('Уже созданная аудитория'))

    def choose_userlist_source(self):
        userlist_source_button = self.find(self.locators.SOURCE_BUTTON_BY_LABEL('Список пользователей'))
        userlist_source_button.click()
        self.find(self.locators.CREATE_NEW_LIST)

    def choose_events_from_announcements_source(self):
        events_from_announcements_source_button = self.find(self.locators.SOURCE_BUTTON_BY_LABEL('События в моих объявлениях'))
        events_from_announcements_source_button.click()

    def choose_audience_source(self):
        self.wait_visibility(self.locators.SOURCE_BUTTON_BY_LABEL('Уже созданная аудитория'))
        self.click(self.locators.SOURCE_BUTTON_BY_LABEL('Уже созданная аудитория'))

    def choose_mobile_categories_source(self):
        mobile_categories_source_button = self.find(self.locators.SOURCE_BUTTON_BY_LABEL('Категории мобильного приложения'))
        mobile_categories_source_button.click()

    def choose_events_from_lead_forms_source(self):
        events_from_lead_forms_source_button = self.find(self.locators.SOURCE_BUTTON_BY_LABEL('События в лид-форме'))
        events_from_lead_forms_source_button.click()
    
    def choose_key_phrases_source(self):
        self.wait_visibility(self.locators.SOURCE_BUTTON_BY_LABEL('Вводили ключевые фразы'))
        self.click(self.locators.SOURCE_BUTTON_BY_LABEL('Вводили ключевые фразы'))

    def choose_community_subscribers_source(self):
        community_subscribers_source_button = self.find(self.locators.SOURCE_BUTTON_BY_LABEL('Подписчики сообществ'))
        community_subscribers_source_button.click()
        self.find(self.locators.ADD_BY_LIST_BUTTON)

    def choose_listeners_source(self):
        listeners_source_button = self.find(self.locators.SOURCE_BUTTON_BY_LABEL('Слушатели музыкантов'))
        listeners_source_button.click()

    def choose_vk_mini_apps_source(self):
        self.wait_visibility(self.locators.SOURCE_BUTTON_BY_LABEL('Пользуются VK Mini Apps'), 25)
        source_button = self.find(self.locators.SOURCE_BUTTON_BY_LABEL('Пользуются VK Mini Apps'))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", source_button)
        source_button.click()

    def create_new_list(self):
        self.wait_visibility(self.locators.CREATE_NEW_LIST)
        create_new_list_button = self.find(self.locators.CREATE_NEW_LIST)
        create_new_list_button.click()

    def set_list_name(self, new_name: str):
        list_name_input = self.find(self.locators.LIST_NAME_INPUT)
        self.driver.execute_script("arguments[0].value = '';", list_name_input)
        list_name_input.send_keys(new_name)

    def set_list_type(self):
        list_type_dropdown = self.find(self.base_locators.DROPDOWN_BY_LABEL('Тип списка'))
        list_type_dropdown.click()
        list_type_dropdown.send_keys(Keys.ARROW_DOWN)
        list_type_dropdown.send_keys(Keys.RETURN)

    def upload_file(self, file_path: str):
        upload_file = self.find(self.locators.UPLOAD_FILE)
        upload_file.send_keys(file_path)

    def set_audience(self):
        list_dropdown = self.find(self.base_locators.DROPDOWN_BY_LABEL("Аудитория"))
        list_dropdown.click()
        self.find(self.locators.OPTION)
        list_dropdown.send_keys(Keys.ARROW_DOWN)
        list_dropdown.send_keys(Keys.RETURN)

    def click_save_button_in_modal(self):
        self.wait_visibility(self.locators.SAVE_IN_MODAL_BUTTON)
        self.click(self.locators.SAVE_IN_MODAL_BUTTON)

    def click_save_button_in_modal_wait(self):
        save_button = self.find(self.locators.SAVE_IN_MODAL_BUTTON)
        save_button.click()
        self.wait_visibility_real(self.locators.OK_DIV)
        self.wait_invisibility(self.locators.OK_DIV)

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
        self.wait_visibility(self.locators.SAVE_BUTTON, timeout=25)
        save_button = self.find(self.locators.SAVE_BUTTON)
        save_button.click()
        self.wait_invisibility(self.locators.SAVE_BUTTON, timeout=15)
    
    def set_musician_name(self, musician_name: str):
        musician_name_input = self.find(self.locators.MUSICIAN_NAME_INPUT)
        musician_name_input.clear()
        musician_name_input.send_keys(musician_name)
        chosen_musician = self.find(self.locators.CHOSEN_MUSICIAN)
        chosen_musician.click()
        complete_button = self.find(self.locators.COMPLETE_BUTTON)
        complete_button.click()
        


    