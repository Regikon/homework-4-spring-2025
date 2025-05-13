from base_case import BaseCase, UserType
from ui.pages.advertiser_sites_page import AdvertiserSitesPage

import time
import pytest



class TestAdvertiserSites(BaseCase):
    user = UserType.ADVERTISER
    PIXEL_DOMAIN = "https://mail.google.com/"
    RENAME = "new_name"
    TOO_LONG_RENAME = "new_name"*255
    RUSSIAN_RENAME = "русское_имя"
    EVENT_NAME = "test_event"
    CATEGORY_NAME = "Покупка"
    CONDITION_NAME = "Посещенная страница"
    URL_CONTAINS = "1"
    DATA_LAYER_OK = "DATA_LAYER_OK"
    DATA_LAYER_RUSSIAN = "абв"
    DATA_LAYER_TOO_LONG = "DATA_LAYER_long"*255
    USER_TO_ACCESS = "24818503"
    AUDITOR_TAG = "auditor_tag"
    ERROR_RUSSIAN = "Недопустимое значение переменной. Используйте только буквы, цифры и символы $, _"
    INSIDE_ERR = "Внутренняя ошибка сервера"


    #@pytest.mark.skip('skip')
    def test_add_pixel(self):
        self.driver.get(AdvertiserSitesPage.url)
        self.advertiser_sites_page =  AdvertiserSitesPage(self.driver)
        self.advertiser_sites_page.add_pixel(self.PIXEL_DOMAIN)
        assert self.advertiser_sites_page.get_pixel_ID_by_href(self.PIXEL_DOMAIN) is not None
        self.advertiser_sites_page.dell_pixel(self.PIXEL_DOMAIN)
        assert self.advertiser_sites_page.get_pixel_ID_by_href(self.PIXEL_DOMAIN) is None

    #@pytest.mark.skip('skip')
    def test_rename_pixel(self):
        self.driver.get(AdvertiserSitesPage.url)
        self.advertiser_sites_page =  AdvertiserSitesPage(self.driver)
        self.advertiser_sites_page.add_pixel(self.PIXEL_DOMAIN)
        self.advertiser_sites_page.rename_pixel(self.PIXEL_DOMAIN, self.RENAME)
        time.sleep(3)
        self.driver.refresh()
        assert self.advertiser_sites_page.SPAN_WITH_TEXT(self.RENAME) is not None 
        self.advertiser_sites_page.dell_pixel(self.PIXEL_DOMAIN)
        assert self.advertiser_sites_page.get_pixel_ID_by_href(self.PIXEL_DOMAIN) is None

    #@pytest.mark.skip('skip')
    def test_too_long_rename_pixel(self):
        self.driver.get(AdvertiserSitesPage.url)
        self.advertiser_sites_page =  AdvertiserSitesPage(self.driver)
        self.advertiser_sites_page.add_pixel(self.PIXEL_DOMAIN)
        self.advertiser_sites_page.rename_pixel(self.PIXEL_DOMAIN, self.TOO_LONG_RENAME)
        time.sleep(3)
        assert self.advertiser_sites_page.find(self.advertiser_sites_page.locators.SPAN_WITH_TEXT(self.INSIDE_ERR)) is not None
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.DISMISS_RENAME)
        self.advertiser_sites_page.dell_pixel(self.PIXEL_DOMAIN)
        assert self.advertiser_sites_page.get_pixel_ID_by_href(self.PIXEL_DOMAIN) is None

    #@pytest.mark.skip('skip')
    def test_data_layer_normal(self):
        self.driver.get(AdvertiserSitesPage.url)
        self.advertiser_sites_page =  AdvertiserSitesPage(self.driver)
        self.advertiser_sites_page.add_pixel(self.PIXEL_DOMAIN)

        self.advertiser_sites_page.click(self.advertiser_sites_page.PIXEL_SETTINGS(self.PIXEL_DOMAIN))
        time.sleep(3)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.CODE_PIXEL_MENU)
        time.sleep(3)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.DATA_LAYER_SWITCH)
        time.sleep(3)
        self.advertiser_sites_page.find(self.advertiser_sites_page.locators.DATA_LAYER_INPUT).send_keys(self.DATA_LAYER_OK)
        time.sleep(3)
        assert self.advertiser_sites_page.find(self.advertiser_sites_page.locators.SPAN_WITH_TEXT(self.ERROR_RUSSIAN)) is None
        assert self.advertiser_sites_page.find(self.advertiser_sites_page.locators.SPAN_WITH_TEXT(self.INSIDE_ERR)) is None

        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.BACK_TO_SITES)
        self.advertiser_sites_page.dell_pixel(self.PIXEL_DOMAIN)

    #@pytest.mark.skip('skip')
    def test_data_layer_russian(self):
        self.driver.get(AdvertiserSitesPage.url)
        self.advertiser_sites_page =  AdvertiserSitesPage(self.driver)
        self.advertiser_sites_page.add_pixel(self.PIXEL_DOMAIN)
        
        time.sleep(3)
        self.advertiser_sites_page.click(self.advertiser_sites_page.PIXEL_SETTINGS(self.PIXEL_DOMAIN))
        time.sleep(3)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.CODE_PIXEL_MENU)
        time.sleep(3)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.DATA_LAYER_SWITCH)
        time.sleep(3)
        self.advertiser_sites_page.find(self.advertiser_sites_page.locators.DATA_LAYER_INPUT).send_keys(self.DATA_LAYER_RUSSIAN)
        time.sleep(3)
        assert self.advertiser_sites_page.find(self.advertiser_sites_page.locators.SPAN_WITH_TEXT(self.ERROR_RUSSIAN)) is not None

        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.BACK_TO_SITES)
        self.advertiser_sites_page.dell_pixel(self.PIXEL_DOMAIN)

    #@pytest.mark.skip('skip')
    def test_data_layer_long(self):
        self.driver.get(AdvertiserSitesPage.url)
        self.advertiser_sites_page =  AdvertiserSitesPage(self.driver)
        self.advertiser_sites_page.add_pixel(self.PIXEL_DOMAIN)
        
        time.sleep(3)
        self.advertiser_sites_page.click(self.advertiser_sites_page.PIXEL_SETTINGS(self.PIXEL_DOMAIN))
        time.sleep(3)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.CODE_PIXEL_MENU)
        time.sleep(3)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.DATA_LAYER_SWITCH)
        time.sleep(3)
        self.advertiser_sites_page.find(self.advertiser_sites_page.locators.DATA_LAYER_INPUT).send_keys(self.DATA_LAYER_TOO_LONG)
        time.sleep(3)
        assert self.advertiser_sites_page.find(self.advertiser_sites_page.locators.SPAN_WITH_TEXT(self.INSIDE_ERR)) is not None

        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.BACK_TO_SITES)
        self.advertiser_sites_page.dell_pixel(self.PIXEL_DOMAIN)
        
    #@pytest.mark.skip('skip')
    def test_add_event_to_pixel(self):
        self.driver.get(AdvertiserSitesPage.url)
        self.advertiser_sites_page =  AdvertiserSitesPage(self.driver)
        self.advertiser_sites_page.add_pixel(self.PIXEL_DOMAIN)

        self.advertiser_sites_page.click(self.advertiser_sites_page.PIXEL_SETTINGS(self.PIXEL_DOMAIN))
        time.sleep(3)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.ADD_EVENT_TO_PIXEL)
        time.sleep(3)
        self.advertiser_sites_page.find(self.advertiser_sites_page.locators.INPUT_EVENT_NAME).send_keys(self.EVENT_NAME)
        time.sleep(3)
        self.advertiser_sites_page.select_category(self.CATEGORY_NAME)
        time.sleep(3)
        self.advertiser_sites_page.select_condition(self.CONDITION_NAME)
        time.sleep(3)
        self.advertiser_sites_page.find(self.advertiser_sites_page.locators.INPUT_URL_CONTAINS).send_keys(self.URL_CONTAINS)
        time.sleep(3)
        self.click(self.advertiser_sites_page.find_one_enabled(self.locators.ADD_EVENT_TO_PIXEL))
        time.sleep(3)
        assert self.advertiser_sites_page.find(self.advertiser_sites_page.locators.SPAN_WITH_TEXT(self.EVENT_NAME)) is not None

        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.BACK_TO_SITES)
        time.sleep(3)
        self.advertiser_sites_page.dell_pixel(self.PIXEL_DOMAIN)
        assert self.advertiser_sites_page.get_pixel_ID_by_href(self.PIXEL_DOMAIN) is None

    #@pytest.mark.skip('skip')
    def test_auditor_tag(self):
        self.driver.get(AdvertiserSitesPage.url)
        self.advertiser_sites_page =  AdvertiserSitesPage(self.driver)
        self.advertiser_sites_page.add_pixel(self.PIXEL_DOMAIN)
        
        time.sleep(3)
        self.advertiser_sites_page.click(self.advertiser_sites_page.PIXEL_SETTINGS(self.PIXEL_DOMAIN))
        time.sleep(3)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.TAGS_PIXEL_MENU)
        time.sleep(3)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.CREATE_TAG_BUTTON)
        time.sleep(3)
        self.advertiser_sites_page.find(self.advertiser_sites_page.locators.TAG_INPUT).send_keys(self.AUDITOR_TAG)
        time.sleep(3)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.TAG_INPUT_BUTTON)
        time.sleep(3)
        self.advertiser_sites_page.hover(self.advertiser_sites_page.locators.TAG_ROW)
        time.sleep(3)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.SHOW_TAG_BUTTON)
        time.sleep(3)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.TAG_CLOSE_BUTTON)
        assert self.advertiser_sites_page.find(self.advertiser_sites_page.locators.SPAN_WITH_TEXT(self.AUDITOR_TAG)) is not None

        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.BACK_TO_SITES)
        self.advertiser_sites_page.dell_pixel(self.PIXEL_DOMAIN)

    #@pytest.mark.skip('skip')
    def test_give_access(self):
        self.driver.get(AdvertiserSitesPage.url)
        self.advertiser_sites_page =  AdvertiserSitesPage(self.driver)
        self.advertiser_sites_page.add_pixel(self.PIXEL_DOMAIN)
        
        time.sleep(3)
        self.advertiser_sites_page.click(self.advertiser_sites_page.PIXEL_SETTINGS(self.PIXEL_DOMAIN))
        time.sleep(3)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.ACCESS_PIXEL_MENU)
        time.sleep(3)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.GIVE_ACCESS_BUTTON)
        time.sleep(3)
        self.advertiser_sites_page.find(self.advertiser_sites_page.locators.ACCESS_INPUT).send_keys(self.USER_TO_ACCESS)
        time.sleep(3)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.ACCESS_GIVE_BUTTON)
        time.sleep(3)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.ACCESS_CLOSE_BUTTON)
        time.sleep(3)
        assert self.advertiser_sites_page.find(self.advertiser_sites_page.locators.SPAN_WITH_TEXT(self.USER_TO_ACCESS)) is not None
        self.advertiser_sites_page.hover(self.advertiser_sites_page.locators.ACCESS_ROW)
        time.sleep(3)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.REVOKE_ACCESS_BUTTON)
        time.sleep(3)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.REVOKE_ACCESS_CONFIRM_BUTTON)
        assert self.advertiser_sites_page.find(self.advertiser_sites_page.locators.SPAN_WITH_TEXT(self.USER_TO_ACCESS)) is None

        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.BACK_TO_SITES)
        self.advertiser_sites_page.dell_pixel(self.PIXEL_DOMAIN)



