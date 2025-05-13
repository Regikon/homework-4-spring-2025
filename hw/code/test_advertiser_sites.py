from base_case import BaseCase, UserType
from ui.pages.advertiser_sites_page import AdvertiserSitesPage
import pytest



class TestAdvertiserSites(BaseCase):
    user = UserType.ADVERTISER
    PIXEL_DOMAIN = "https://uart.site/"
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
    USER_TO_ACCESS = "14718513"
    AUDITOR_TAG = "Some strange name"
    ERROR_RUSSIAN = "Недопустимое значение переменной. Используйте только буквы, цифры и символы $, _"
    INSIDE_ERR = "Внутренняя ошибка сервера"


    #@pytest.mark.skip('skip')
    def test_add_pixel(self):
        self.driver.get(AdvertiserSitesPage.url)
        self.advertiser_sites_page =  AdvertiserSitesPage(self.driver)
        self.advertiser_sites_page.add_pixel(self.PIXEL_DOMAIN)
        assert self.advertiser_sites_page.get_pixel_ID_by_href(self.PIXEL_DOMAIN) is not None
        self.advertiser_sites_page.dell_pixel(self.PIXEL_DOMAIN)
        self.advertiser_sites_page.reload()
        assert self.advertiser_sites_page.get_pixel_ID_by_href(self.PIXEL_DOMAIN) is None

    #@pytest.mark.skip('skip')
    def test_rename_pixel(self):
        self.driver.get(AdvertiserSitesPage.url)
        self.advertiser_sites_page =  AdvertiserSitesPage(self.driver)
        self.advertiser_sites_page.add_pixel(self.PIXEL_DOMAIN)
        self.advertiser_sites_page.rename_pixel(self.PIXEL_DOMAIN, self.RENAME)
        self.advertiser_sites_page.reload()
        assert not self.advertiser_sites_page.has_element(self.advertiser_sites_page.SPAN_WITH_TEXT(self.RENAME))
        self.advertiser_sites_page.dell_pixel(self.PIXEL_DOMAIN)
        assert self.advertiser_sites_page.get_pixel_ID_by_href(self.PIXEL_DOMAIN) is None

    #@pytest.mark.skip('skip')
    def test_too_long_rename_pixel(self):
        self.driver.get(AdvertiserSitesPage.url)
        self.advertiser_sites_page =  AdvertiserSitesPage(self.driver)
        self.advertiser_sites_page.add_pixel(self.PIXEL_DOMAIN)
        self.advertiser_sites_page.rename_pixel(self.PIXEL_DOMAIN, self.TOO_LONG_RENAME)
        assert self.advertiser_sites_page.has_element(self.advertiser_sites_page.locators.DIV_ERROR)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.DISMISS_RENAME)
        self.advertiser_sites_page.dell_pixel(self.PIXEL_DOMAIN)

    #@pytest.mark.skip('skip')
    def test_data_layer_normal(self):
        self.driver.get(AdvertiserSitesPage.url)
        self.advertiser_sites_page =  AdvertiserSitesPage(self.driver)
        self.advertiser_sites_page.add_pixel(self.PIXEL_DOMAIN)
        self.advertiser_sites_page.click(self.advertiser_sites_page.PIXEL_SETTINGS(self.PIXEL_DOMAIN))
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.CODE_PIXEL_MENU)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.DATA_LAYER_SWITCH)
        self.advertiser_sites_page.find(self.advertiser_sites_page.locators.DATA_LAYER_INPUT).send_keys(self.DATA_LAYER_OK)
        assert not self.advertiser_sites_page.has_element(self.advertiser_sites_page.SPAN_WITH_TEXT(self.ERROR_RUSSIAN))
        assert not self.advertiser_sites_page.has_element(self.advertiser_sites_page.SPAN_WITH_TEXT(self.INSIDE_ERR))
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.BACK_TO_SITES)
        self.advertiser_sites_page.dell_pixel(self.PIXEL_DOMAIN)

    #@pytest.mark.skip('skip')
    def test_data_layer_russian(self):
        self.driver.get(AdvertiserSitesPage.url)
        self.advertiser_sites_page =  AdvertiserSitesPage(self.driver)
        self.advertiser_sites_page.add_pixel(self.PIXEL_DOMAIN)
        self.advertiser_sites_page.click(self.advertiser_sites_page.PIXEL_SETTINGS(self.PIXEL_DOMAIN))
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.CODE_PIXEL_MENU)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.DATA_LAYER_SWITCH)
        self.advertiser_sites_page.find(self.advertiser_sites_page.locators.DATA_LAYER_INPUT).send_keys(self.DATA_LAYER_RUSSIAN)
        assert self.advertiser_sites_page.has_element(self.advertiser_sites_page.SPAN_WITH_TEXT(self.ERROR_RUSSIAN))
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.BACK_TO_SITES)
        self.advertiser_sites_page.dell_pixel(self.PIXEL_DOMAIN)

    #@pytest.mark.skip('skip')
    def test_data_layer_long(self):
        self.driver.get(AdvertiserSitesPage.url)
        self.advertiser_sites_page =  AdvertiserSitesPage(self.driver)
        self.advertiser_sites_page.add_pixel(self.PIXEL_DOMAIN)
        self.advertiser_sites_page.click(self.advertiser_sites_page.PIXEL_SETTINGS(self.PIXEL_DOMAIN))
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.CODE_PIXEL_MENU)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.DATA_LAYER_SWITCH)
        self.advertiser_sites_page.find(self.advertiser_sites_page.locators.DATA_LAYER_INPUT).send_keys(self.DATA_LAYER_TOO_LONG)
        assert self.advertiser_sites_page.has_element(self.advertiser_sites_page.SPAN_WITH_TEXT(self.INSIDE_ERR))
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.BACK_TO_SITES)
        self.advertiser_sites_page.dell_pixel(self.PIXEL_DOMAIN)
        
    #@pytest.mark.skip('skip')
    def test_add_event_to_pixel(self):
        self.driver.get(AdvertiserSitesPage.url)
        self.advertiser_sites_page =  AdvertiserSitesPage(self.driver)
        self.advertiser_sites_page.add_pixel(self.PIXEL_DOMAIN)
        self.advertiser_sites_page.click(self.advertiser_sites_page.PIXEL_SETTINGS(self.PIXEL_DOMAIN))
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.ADD_EVENT_TO_PIXEL)
        self.advertiser_sites_page.find(self.advertiser_sites_page.locators.INPUT_EVENT_NAME).send_keys(self.EVENT_NAME)
        self.advertiser_sites_page.select_category(self.CATEGORY_NAME)
        self.advertiser_sites_page.select_condition(self.CONDITION_NAME)
        self.advertiser_sites_page.find(self.advertiser_sites_page.locators.INPUT_URL_CONTAINS).send_keys(self.URL_CONTAINS)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.ADD_EVENT_TO_PIXEL_CONFIRM)
        assert self.advertiser_sites_page.has_element(self.advertiser_sites_page.SPAN_WITH_TEXT(self.EVENT_NAME))
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.BACK_TO_SITES)
        self.advertiser_sites_page.dell_pixel(self.PIXEL_DOMAIN)

    #@pytest.mark.skip('skip')
    def test_auditor_tag(self):
        self.driver.get(AdvertiserSitesPage.url)
        self.advertiser_sites_page =  AdvertiserSitesPage(self.driver)
        self.advertiser_sites_page.add_pixel(self.PIXEL_DOMAIN)
        self.advertiser_sites_page.click(self.advertiser_sites_page.PIXEL_SETTINGS(self.PIXEL_DOMAIN))
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.TAGS_PIXEL_MENU)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.CREATE_TAG_BUTTON)
        self.advertiser_sites_page.find(self.advertiser_sites_page.locators.TAG_INPUT).send_keys(self.AUDITOR_TAG)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.TAG_INPUT_BUTTON)
        self.advertiser_sites_page.sub_element(self.advertiser_sites_page.locators.TAG_ROW, self.advertiser_sites_page.locators.SHOW_TAG_BUTTON)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.TAG_CLOSE_BUTTON)
        self.advertiser_sites_page.reload()
        assert self.advertiser_sites_page.has_element(self.advertiser_sites_page.DIV_WITH_TEXT(self.AUDITOR_TAG))
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.BACK_TO_SITES)
        self.advertiser_sites_page.dell_pixel(self.PIXEL_DOMAIN)

    #@pytest.mark.skip('skip')
    def test_give_access(self):
        self.driver.get(AdvertiserSitesPage.url)
        self.advertiser_sites_page =  AdvertiserSitesPage(self.driver)
        self.advertiser_sites_page.add_pixel(self.PIXEL_DOMAIN)
        self.advertiser_sites_page.click(self.advertiser_sites_page.PIXEL_SETTINGS(self.PIXEL_DOMAIN))
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.ACCESS_PIXEL_MENU)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.GIVE_ACCESS_BUTTON)
        self.advertiser_sites_page.find(self.advertiser_sites_page.locators.ACCESS_INPUT).send_keys(self.USER_TO_ACCESS)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.ACCESS_GIVE_BUTTON)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.ACCESS_CLOSE_BUTTON)
        assert self.advertiser_sites_page.has_element(self.advertiser_sites_page.SPAN_WITH_TEXT(self.USER_TO_ACCESS))
        self.advertiser_sites_page.sub_element(self.advertiser_sites_page.locators.ACCESS_ROW, self.advertiser_sites_page.locators.REVOKE_ACCESS_BUTTON)
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.REVOKE_ACCESS_CONFIRM_BUTTON)
        self.advertiser_sites_page.reload()
        assert not self.advertiser_sites_page.has_element(self.advertiser_sites_page.DIV_WITH_TEXT(self.USER_TO_ACCESS))
        self.advertiser_sites_page.click(self.advertiser_sites_page.locators.BACK_TO_SITES)
        self.advertiser_sites_page.dell_pixel(self.PIXEL_DOMAIN)



