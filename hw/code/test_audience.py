from base_case import BaseCase, UserType
from ui.pages.audience_page import AudiencePage
import os
from time import sleep

import pytest

class TestAddUserlist(BaseCase):
    user = UserType.ADVERTISER

    def test_add_new_list(self):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_audience_page = audience_page.go_to_add_userlist_page()
        add_audience_page.set_list_name("test_add_new_list")
        add_audience_page.set_list_type()
        add_audience_page.upload_file(os.path.abspath("hw/code/files/union_list.csv"))
        add_audience_page.set_not_create_new_audience()
        add_audience_page.click_save_button()
        assert audience_page.has_userlist_with_name("test_add_new_list")
    
    def test_add_to_existing_list(self):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        audience_page.go_to_userlist()
        current_identifier = audience_page.get_current_identifier()
        add_audience_page = audience_page.go_to_add_userlist_page()
        add_audience_page.switch_to_add_to_existing_list()
        add_audience_page.set_list()
        add_audience_page.upload_file(os.path.abspath("hw/code/files/generated_data_250.csv"))
        add_audience_page.click_save_button()
        audience_page.has_success_message()
        self.driver.refresh()
        new_identifier = audience_page.get_current_identifier()
        assert new_identifier > current_identifier

    def test_exclude_from_existing_list(self):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        audience_page.go_to_userlist()
        current_identifier = audience_page.get_current_identifier()
        add_audience_page = audience_page.go_to_add_userlist_page()
        add_audience_page.switch_to_exclude_from_existing_list()
        add_audience_page.set_list_exclude()
        add_audience_page.upload_file(os.path.abspath("hw/code/files/generated_data_250.csv"))
        add_audience_page.click_save_button()
        audience_page.has_success_message()
        self.driver.refresh()
        new_identifier = audience_page.get_current_identifier()
        assert new_identifier < current_identifier

    def test_delete_list(self):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        audience_page.go_to_userlist()
        audience_page.delete_userlist("test_add_new_list")
        self.driver.refresh()
        assert not audience_page.has_userlist_with_name("test_add_new_list")

class TestAddAudience(BaseCase):
    user = UserType.ADVERTISER

    @pytest.mark.skip('skip')
    def test_add_userlist_source(self):
        pass

    @pytest.mark.skip('skip')
    def test_exclude_userlist_source(self):
        pass

    @pytest.mark.skip('skip')
    def test_add_existing_audience_source(self):
        pass

    @pytest.mark.skip('skip')
    def test_add_event_from_announcements_source(self):
        pass

    @pytest.mark.skip('skip')
    def test_add_mobile_category_source(self):
        pass

    @pytest.mark.skip('skip')
    def test_add_event_from_lead_form_source(self):
        pass

    @pytest.mark.skip('skip')
    def test_add_key_phrases_source(self):
        pass

    @pytest.mark.skip('skip')
    def test_add_subscribers_source(self):
        pass

    @pytest.mark.skip('skip')
    def test_add_listeners_source(self):
        pass

    @pytest.mark.skip('skip')
    def test_add_vk_mini_apps_source(self):
        pass

    @pytest.mark.skip('skip')
    def test_delete_audience(self):
        pass

class TestAddOfflineConversion(BaseCase):
    user = UserType.ADVERTISER

    @pytest.mark.skip('skip')
    def test_add_new_offline_conversion(self):
        pass

    @pytest.mark.skip('skip')
    def test_add_to_existing_offline_conversion(self):
        pass