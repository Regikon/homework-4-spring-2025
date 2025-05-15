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
        add_userlist_page = audience_page.go_to_add_userlist_page()
        add_userlist_page.set_list_name("test_add_new_list")
        add_userlist_page.set_list_type()
        add_userlist_page.upload_file(os.path.abspath("hw/code/files/union_list.csv"))
        add_userlist_page.set_not_create_new_audience()
        add_userlist_page.click_save_button()
        assert audience_page.has_userlist_with_name("test_add_new_list")

    def test_add_to_existing_list(self):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        audience_page.go_to_userlist()
        current_identifier = audience_page.get_current_identifier()
        add_userlist_page = audience_page.go_to_add_userlist_page()
        add_userlist_page.switch_to_add_to_existing_list()
        add_userlist_page.set_list()
        add_userlist_page.upload_file(os.path.abspath("hw/code/files/generated_data_250.csv"))
        add_userlist_page.click_save_button()
        audience_page.has_success_message()
        self.driver.refresh()
        new_identifier = audience_page.get_current_identifier()
        assert new_identifier >= current_identifier

    def test_exclude_from_existing_list(self):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        audience_page.go_to_userlist()
        current_identifier = audience_page.get_current_identifier()
        add_userlist_page = audience_page.go_to_add_userlist_page()
        add_userlist_page.switch_to_exclude_from_existing_list()
        add_userlist_page.set_list_exclude()
        add_userlist_page.upload_file(os.path.abspath("hw/code/files/generated_data_250.csv"))
        add_userlist_page.click_save_button()
        audience_page.has_success_message()
        self.driver.refresh()
        new_identifier = audience_page.get_current_identifier()
        assert new_identifier <= current_identifier

    def test_delete_list(self):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        audience_page.go_to_userlist()
        audience_page.delete_userlist("test_add_new_list")
        self.driver.refresh()
        assert not audience_page.has_userlist_with_name("test_add_new_list")

class TestAddAudience(BaseCase):
    user = UserType.ADVERTISER

    def test_add_userlist_source(self):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_audience_page = audience_page.go_to_add_audience_page()
        add_audience_page.set_name("test_add_userlist_source")
        add_audience_page.add_source()
        add_audience_page.choose_userlist_source()
        add_audience_page.create_new_list()
        add_audience_page.set_list_name("test_add_userlist_source")
        add_audience_page.set_list_type()
        add_audience_page.upload_file(os.path.abspath("hw/code/files/union_list.csv"))
        add_audience_page.click_save_button_in_modal_wait()
        add_audience_page.click_save_button()
        assert audience_page.has_audience_with_name("test_add_userlist_source")

    def test_delete_audience(self):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        audience_page.delete_audience("test_add_userlist_source")
        self.driver.refresh()
        assert not audience_page.has_userlist_with_name("test_add_userlist_source")

    def test_exclude_userlist_source(self):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_audience_page = audience_page.go_to_add_audience_page()
        add_audience_page.set_name("test_exclude_userlist_source")
        add_audience_page.exclude_source()
        add_audience_page.choose_userlist_source()
        add_audience_page.create_new_list()
        add_audience_page.set_list_name("test_add_userlist_source")
        add_audience_page.set_list_type()
        add_audience_page.upload_file(os.path.abspath("hw/code/files/union_list.csv"))
        add_audience_page.click_save_button_in_modal_wait()
        add_audience_page.click_save_button()
        assert audience_page.has_audience_with_name("test_exclude_userlist_source")

    @pytest.mark.skip('skip')
    def test_add_existing_audience_source(self):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_audience_page = audience_page.go_to_add_audience_page()
        add_audience_page.set_name("test_add_existing_audience_source")
        add_audience_page.add_source()
        add_audience_page.choose_audience_source()
        add_audience_page.set_audience()
        add_audience_page.click_save_button_in_modal()
        add_audience_page.click_save_button()
        assert audience_page.has_audience_with_name("test_add_existing_audience_source")

    @pytest.mark.skip('skip')
    def test_add_key_phrases_source(self):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_audience_page = audience_page.go_to_add_audience_page()
        add_audience_page.set_name("test_add_key_phrases_source")
        add_audience_page.add_source()
        add_audience_page.choose_key_phrases_source()
        add_audience_page.add_key_phrase("test key phrase")
        add_audience_page.click_save_button_in_modal()
        add_audience_page.click_save_button()
        assert audience_page.has_audience_with_name("test_add_key_phrases_source")

    #@pytest.mark.skip('skip')
    def test_add_subscribers_source(self):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_audience_page = audience_page.go_to_add_audience_page()
        add_audience_page.set_name("test_add_subscribers_source")
        add_audience_page.add_source()
        add_audience_page.choose_community_subscribers_source()
        add_audience_page.add_communtity("https://vk.com/son_sovy")
        add_audience_page.click_save_button_in_modal()
        add_audience_page.click_save_button()
        assert audience_page.has_audience_with_name("test_add_subscribers_source")

    @pytest.mark.skip('skip')
    def test_add_listeners_source(self):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_audience_page = audience_page.go_to_add_audience_page()
        add_audience_page.set_name("test_add_listeners_source")
        add_audience_page.add_source()
        add_audience_page.choose_listeners_source()
        add_audience_page.set_musician_name("Lizer")
        add_audience_page.click_save_button_in_modal()
        add_audience_page.click_save_button()
        assert audience_page.has_audience_with_name("test_add_listeners_source")

    #@pytest.mark.skip('skip')
    def test_add_vk_mini_apps_source(self):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_audience_page = audience_page.go_to_add_audience_page()
        add_audience_page.set_name("test_add_vk_mini_apps_source")
        add_audience_page.add_source()
        add_audience_page.choose_vk_mini_apps_source()
        add_audience_page.add_app("https://vk.com/app4670469")
        add_audience_page.click_save_button_in_modal()
        add_audience_page.click_save_button()
        assert audience_page.has_audience_with_name("test_add_vk_mini_apps_source")


    #тут и было закоменчено

    @pytest.mark.skip('skip')
    def test_add_event_from_announcements_source(self):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_audience_page = audience_page.go_to_add_audience_page()
        add_audience_page.set_name("test_add_event_from_announcements_source")
        add_audience_page.add_source()
        add_audience_page.choose_events_from_announcements_source()
        pass

    @pytest.mark.skip('skip')
    def test_add_mobile_category_source(self):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_audience_page = audience_page.go_to_add_audience_page()
        add_audience_page.set_name("test_add_mobile_category_source")
        add_audience_page.add_source()
        add_audience_page.choose_mobile_categories_source()
        pass

    @pytest.mark.skip('skip')
    def test_add_event_from_lead_form_source(self):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_audience_page = audience_page.go_to_add_audience_page()
        add_audience_page.set_name("test_add_event_from_lead_form_source")
        add_audience_page.add_source()
        add_audience_page.choose_events_from_lead_forms_source()
        pass

class TestAddOfflineConversion(BaseCase):
    user = UserType.ADVERTISER

    # 503 Service Unavailable
    @pytest.mark.skip('skip')
    def test_add_new_offline_conversion(self):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_offline_conversion_page = audience_page.go_to_add_offline_conversion_page()
        add_offline_conversion_page.choose_create_new_list()
        add_offline_conversion_page.set_list_name("conversion_users_plain_phones")
        add_offline_conversion_page.set_list_type()
        add_offline_conversion_page.upload_file(os.path.abspath("hw/code/files/conversion_users_plain_phones.csv"))
        add_offline_conversion_page.click_save_button()
        assert audience_page.has_offline_conversion_with_name("conversion_users_plain_phones")

    # 503 Service Unavailable
    @pytest.mark.skip('skip')
    def test_add_to_existing_offline_conversion(self):
        self.driver.get(AudiencePage.url)
        audience_page = AudiencePage(self.driver)
        add_offline_conversion_page = audience_page.go_to_add_offline_conversion_page()
        add_offline_conversion_page.choose_add_to_existing_list()
        pass