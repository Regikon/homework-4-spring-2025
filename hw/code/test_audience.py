from base_case import BaseCase, UserType
from ui.pages.audience_page import AudiencePage
from ui.pages.audience_add_userlist_page import AudienceAddUserlistPage
import os
import pytest
import re

@pytest.fixture(scope="function")
def cleanup_registry(driver):
    to_delete = []
    yield to_delete
    driver.get(AudiencePage.url)
    page = AudiencePage(driver)
    for obj_type, name in to_delete:
        if obj_type == "audience":
            if driver.current_url != AudiencePage.url:
                page.go_to_audience_page()
            page.delete_audience(name)
        elif obj_type == "userlist":
            if driver.current_url != AudienceAddUserlistPage.url:
                page.go_to_userlist()
            page.delete_userlist(name)

@pytest.fixture(scope="function")
def prepared_userlist(driver):
    name = "test_add_new_list"
    path_to_file = "hw/code/files/union_list.csv"
    driver.get(AudiencePage.url)
    page = AudiencePage(driver)
    add_page = page.go_to_add_userlist_page()
    add_page.set_list_name(name)
    add_page.set_list_type()
    add_page.upload_file(os.path.abspath(path_to_file))
    add_page.set_not_create_new_audience()
    add_page.click_save_button()
    yield name 
    driver.get(AudiencePage.url)
    page = AudiencePage(driver)
    if driver.current_url != AudienceAddUserlistPage.url:
        page.go_to_userlist()
    try:
        page.delete_userlist(name)
    except Exception as e:
        print(f"Error deleting userlist {name}: {e}")

def get_identifier(tooltip):
    text = tooltip.text
    match = re.search(r'\d+', text)
    return float(match.group())

class TestAddUserlist(BaseCase):
    user = UserType.ADVERTISER

    OBJ_TYPE_USERLIST = "userlist"
    PATH_TO_FILE_UNION_LIST = "hw/code/files/union_list.csv"
    PATH_TO_FILE_GENERATED_DATA = "hw/code/files/generated_data_250.csv"
    CORRECT_NAME = "test_add_new_list"

    def test_add_new_list(self, cleanup_registry):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_userlist_page = audience_page.go_to_add_userlist_page()
        add_userlist_page.set_list_name(self.CORRECT_NAME)
        add_userlist_page.set_list_type()
        add_userlist_page.upload_file(os.path.abspath(self.PATH_TO_FILE_UNION_LIST))
        add_userlist_page.set_not_create_new_audience()
        add_userlist_page.click_save_button()
        cleanup_registry.append((self.OBJ_TYPE_USERLIST, self.CORRECT_NAME))
        assert audience_page.has_element(AudiencePage.locators.USERLIST_BY_NAME(self.CORRECT_NAME))

    def test_add_to_existing_list(self, prepared_userlist):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        audience_page.go_to_userlist()
        audience_page.open_status()
        tooltip = audience_page.find(AudiencePage.locators.HINT)
        current_identifier = get_identifier(tooltip)
        add_userlist_page = audience_page.go_to_add_userlist_page()
        add_userlist_page.switch_to_add_to_existing_list()
        add_userlist_page.set_list()
        add_userlist_page.upload_file(os.path.abspath(self.PATH_TO_FILE_GENERATED_DATA))
        add_userlist_page.click_save_button()
        audience_page.has_success_message()
        audience_page.open_status()
        tooltip = audience_page.find(AudiencePage.locators.HINT)
        new_identifier = get_identifier(tooltip)
        assert new_identifier >= current_identifier

    def test_exclude_from_existing_list(self, prepared_userlist):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        audience_page.go_to_userlist()
        audience_page.open_status()
        tooltip = audience_page.find(AudiencePage.locators.HINT)
        current_identifier = get_identifier(tooltip)
        add_userlist_page = audience_page.go_to_add_userlist_page()
        add_userlist_page.switch_to_exclude_from_existing_list()
        add_userlist_page.set_list_exclude()
        add_userlist_page.upload_file(os.path.abspath(self.PATH_TO_FILE_GENERATED_DATA))
        add_userlist_page.click_save_button()
        audience_page.has_success_message()
        audience_page.open_status()
        tooltip = audience_page.find(AudiencePage.locators.HINT)
        new_identifier = get_identifier(tooltip)
        assert new_identifier <= current_identifier

    def test_delete_list(self, prepared_userlist):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        audience_page.go_to_userlist()
        audience_page.delete_userlist(self.CORRECT_NAME)
        self.driver.refresh()
        assert not audience_page.has_element(AudiencePage.locators.USERLIST_BY_NAME(self.CORRECT_NAME))

class TestAddAudience(BaseCase):
    user = UserType.ADVERTISER

    OBJ_TYPE_USERLIST = "userlist"
    OBJ_TYPE_AUDIENCE = "audience"
    PATH_TO_FILE_UNION_LIST = "hw/code/files/union_list.csv"
    CORRECT_NAME = "test_add_audience"
    CORRECT_NAME_V2 = "test_add_audience_v2"
    KEY_PHRASE = "test key phrase"
    LINK_TO_COMMUNITY = "https://vk.com/son_sovy"
    MUSICIAN_NAME = "Lizer"
    LINK_TO_APP = "https://vk.com/app4670469"

    def test_add_userlist_source(self, cleanup_registry):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_audience_page = audience_page.go_to_add_audience_page()
        add_audience_page.set_name(self.CORRECT_NAME)
        add_audience_page.add_source()
        add_audience_page.choose_userlist_source()
        add_audience_page.create_new_list()
        add_audience_page.set_list_name(self.CORRECT_NAME)
        add_audience_page.set_list_type()
        add_audience_page.upload_file(os.path.abspath(self.PATH_TO_FILE_UNION_LIST))
        add_audience_page.click_save_button_in_modal_wait()
        add_audience_page.click_save_button()
        cleanup_registry.append((self.OBJ_TYPE_AUDIENCE, self.CORRECT_NAME))
        cleanup_registry.append((self.OBJ_TYPE_USERLIST, self.CORRECT_NAME))
        assert audience_page.has_element(AudiencePage.locators.AUDIENCE_BY_NAME(self.CORRECT_NAME))

    def test_delete_audience(self, cleanup_registry):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_audience_page = audience_page.go_to_add_audience_page()
        add_audience_page.set_name(self.CORRECT_NAME)
        add_audience_page.add_source()
        add_audience_page.choose_userlist_source()
        add_audience_page.create_new_list()
        add_audience_page.set_list_name(self.CORRECT_NAME)
        add_audience_page.set_list_type()
        add_audience_page.upload_file(os.path.abspath(self.PATH_TO_FILE_UNION_LIST))
        add_audience_page.click_save_button_in_modal_wait()
        add_audience_page.click_save_button()
        cleanup_registry.append((self.OBJ_TYPE_USERLIST, self.CORRECT_NAME))
        audience_page.delete_audience(self.CORRECT_NAME)
        audience_page.reload()
        assert not audience_page.has_element(AudiencePage.locators.AUDIENCE_BY_NAME(self.CORRECT_NAME))

    def test_exclude_userlist_source(self, cleanup_registry):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_audience_page = audience_page.go_to_add_audience_page()
        add_audience_page.set_name(self.CORRECT_NAME)
        add_audience_page.exclude_source()
        add_audience_page.choose_userlist_source()
        add_audience_page.create_new_list()
        add_audience_page.set_list_name(self.CORRECT_NAME)
        add_audience_page.set_list_type()
        add_audience_page.upload_file(os.path.abspath(self.PATH_TO_FILE_UNION_LIST))
        add_audience_page.click_save_button_in_modal_wait()
        add_audience_page.click_save_button()
        cleanup_registry.append((self.OBJ_TYPE_AUDIENCE, self.CORRECT_NAME))
        cleanup_registry.append((self.OBJ_TYPE_USERLIST, self.CORRECT_NAME))
        assert audience_page.has_element(AudiencePage.locators.AUDIENCE_BY_NAME(self.CORRECT_NAME))

    def test_add_existing_audience_source(self, cleanup_registry):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_audience_page = audience_page.go_to_add_audience_page()
        add_audience_page.set_name(self.CORRECT_NAME)
        add_audience_page.add_source()
        add_audience_page.choose_userlist_source()
        add_audience_page.create_new_list()
        add_audience_page.set_list_name(self.CORRECT_NAME)
        add_audience_page.set_list_type()
        add_audience_page.upload_file(os.path.abspath(self.PATH_TO_FILE_UNION_LIST))
        add_audience_page.click_save_button_in_modal_wait()
        add_audience_page.click_save_button()
        add_audience_page = audience_page.go_to_add_audience_page()
        add_audience_page.set_name(self.CORRECT_NAME_V2)
        add_audience_page.add_source()
        add_audience_page.choose_audience_source()
        add_audience_page.set_audience()
        add_audience_page.click_save_button_in_modal()
        add_audience_page.click_save_button()
        cleanup_registry.append((self.OBJ_TYPE_AUDIENCE, self.CORRECT_NAME_V2))
        cleanup_registry.append((self.OBJ_TYPE_AUDIENCE, self.CORRECT_NAME))
        cleanup_registry.append((self.OBJ_TYPE_USERLIST, self.CORRECT_NAME))
        assert audience_page.has_element(AudiencePage.locators.AUDIENCE_BY_NAME(self.CORRECT_NAME_V2))

    def test_add_key_phrases_source(self, cleanup_registry):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_audience_page = audience_page.go_to_add_audience_page()
        add_audience_page.set_name(self.CORRECT_NAME)
        add_audience_page.add_source()
        add_audience_page.choose_key_phrases_source()
        add_audience_page.add_key_phrase(self.KEY_PHRASE)
        add_audience_page.click_save_button_in_modal()
        add_audience_page.click_save_button()
        cleanup_registry.append((self.OBJ_TYPE_AUDIENCE, self.CORRECT_NAME))
        assert audience_page.has_element(AudiencePage.locators.AUDIENCE_BY_NAME(self.CORRECT_NAME))

    def test_add_subscribers_source(self, cleanup_registry):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_audience_page = audience_page.go_to_add_audience_page()
        add_audience_page.set_name(self.CORRECT_NAME)
        add_audience_page.add_source()
        add_audience_page.choose_community_subscribers_source()
        add_audience_page.add_communtity(self.LINK_TO_COMMUNITY)
        add_audience_page.click_save_button_in_modal()
        add_audience_page.click_save_button()
        cleanup_registry.append((self.OBJ_TYPE_AUDIENCE, self.CORRECT_NAME))
        assert audience_page.has_element(AudiencePage.locators.AUDIENCE_BY_NAME(self.CORRECT_NAME))

    def test_add_listeners_source(self, cleanup_registry):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_audience_page = audience_page.go_to_add_audience_page()
        add_audience_page.set_name(self.CORRECT_NAME)
        add_audience_page.add_source()
        add_audience_page.choose_listeners_source()
        add_audience_page.set_musician_name(self.MUSICIAN_NAME)
        add_audience_page.click_save_button_in_modal()
        add_audience_page.click_save_button()
        cleanup_registry.append((self.OBJ_TYPE_AUDIENCE, self.CORRECT_NAME))
        assert audience_page.has_element(AudiencePage.locators.AUDIENCE_BY_NAME(self.CORRECT_NAME))

    def test_add_vk_mini_apps_source(self, cleanup_registry):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_audience_page = audience_page.go_to_add_audience_page()
        add_audience_page.set_name(self.CORRECT_NAME)
        add_audience_page.add_source()
        add_audience_page.choose_vk_mini_apps_source()
        add_audience_page.add_app(self.LINK_TO_APP)
        add_audience_page.click_save_button_in_modal()
        add_audience_page.click_save_button()
        cleanup_registry.append((self.OBJ_TYPE_AUDIENCE, self.CORRECT_NAME))
        assert audience_page.has_element(AudiencePage.locators.AUDIENCE_BY_NAME(self.CORRECT_NAME))

class TestAddOfflineConversion(BaseCase):
    user = UserType.ADVERTISER

    CORRECT_NAME = "test_add_offline_conversion"
    PATH_TO_FILE_PHONES = "hw/code/files/conversion_users_plain_phones.csv"

    # 503 Service Unavailable. 
    # Unable to create offline conversion.
    @pytest.mark.skip('skip')
    def test_add_new_offline_conversion(self):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_offline_conversion_page = audience_page.go_to_add_offline_conversion_page()
        add_offline_conversion_page.choose_create_new_list()
        add_offline_conversion_page.set_list_name(self.CORRECT_NAME)
        add_offline_conversion_page.set_list_type()
        add_offline_conversion_page.upload_file(os.path.abspath(self.PATH_TO_FILE_PHONES))
        add_offline_conversion_page.click_save_button()
        assert audience_page.has_element(AudiencePage.locators.OFFLINE_CONVERSION_BY_NAME(self.CORRECT_NAME))

    # 503 Service Unavailable
    # Unable to create offline conversion.
    @pytest.mark.skip('skip')
    def test_add_to_existing_offline_conversion(self):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_offline_conversion_page = audience_page.go_to_add_offline_conversion_page()
        add_offline_conversion_page.choose_add_to_existing_list()