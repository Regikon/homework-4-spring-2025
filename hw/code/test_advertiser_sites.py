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
    URL_CONTAINS = "1"
    DATA_LAYER_OK = "DATA_LAYER_OK"
    DATA_LAYER_RUSSIAN = "абв"
    DATA_LAYER_TOO_LONG = "DATA_LAYER_long"*255
    USER_TO_ACCESS = "14718513"
    AUDITOR_TAG = "Some strange name"
    ERROR_RUSSIAN = "Недопустимое значение переменной. Используйте только буквы, цифры и символы $, _"
    INSIDE_ERR = "Внутренняя ошибка сервера"

    def test_add_pixel(self):
        self.driver.get(AdvertiserSitesPage.url)
        page = AdvertiserSitesPage(self.driver)
        page.add_pixel(self.PIXEL_DOMAIN)
        assert page.get_pixel_ID_by_href(self.PIXEL_DOMAIN) is not None
        page.dell_pixel(self.PIXEL_DOMAIN)
        page.reload()
        assert page.get_pixel_ID_by_href(self.PIXEL_DOMAIN) is None

    @pytest.mark.parametrize('pixel', [PIXEL_DOMAIN], indirect=True)
    def test_rename_pixel1(self, pixel):
        page, pixel = pixel[0], pixel[1]
        page.rename_pixel(pixel, self.RENAME)
        page.reload()
        assert not page.has_element(AdvertiserSitesPage.locators.SPAN_WITH_TEXT(self.RENAME))

    @pytest.mark.parametrize('pixel', [PIXEL_DOMAIN], indirect=True)
    def test_rename_pixel(self, pixel):
        page, pixel = pixel[0], pixel[1]
        page.rename_pixel(self.PIXEL_DOMAIN, self.RENAME)
        page.reload()
        assert not page.has_element(AdvertiserSitesPage.locators.SPAN_WITH_TEXT(self.RENAME))


    @pytest.mark.parametrize('pixel', [PIXEL_DOMAIN], indirect=True)
    def test_too_long_rename_pixel(self, pixel):
        page, pixel = pixel[0], pixel[1]
        page.rename_pixel(self.PIXEL_DOMAIN, self.TOO_LONG_RENAME)
        assert page.has_err_in_div()
        page.cancel_rename()

    @pytest.mark.parametrize('pixel', [PIXEL_DOMAIN], indirect=True)
    def test_data_layer_normal(self, pixel):
        page, pixel = pixel[0], pixel[1]
        page.click(page.PIXEL_SETTINGS(self.PIXEL_DOMAIN))
        page.code_pixel_text_correct(self.DATA_LAYER_OK)
        assert not page.has_element(AdvertiserSitesPage.locators.SPAN_WITH_TEXT(self.ERROR_RUSSIAN))
        assert not page.has_element(AdvertiserSitesPage.locators.SPAN_WITH_TEXT(self.INSIDE_ERR))

    @pytest.mark.parametrize('pixel', [PIXEL_DOMAIN], indirect=True)
    def test_data_layer_russian(self, pixel):
        page, pixel = pixel[0], pixel[1]
        page.click(page.PIXEL_SETTINGS(self.PIXEL_DOMAIN))
        page.code_pixel_text_correct(self.DATA_LAYER_RUSSIAN)
        assert page.has_element(AdvertiserSitesPage.locators.SPAN_WITH_TEXT(self.ERROR_RUSSIAN))

    @pytest.mark.parametrize('pixel', [PIXEL_DOMAIN], indirect=True)
    def test_data_layer_long(self, pixel):
        page, pixel = pixel[0], pixel[1]
        page.click(page.PIXEL_SETTINGS(self.PIXEL_DOMAIN))
        page.code_pixel_text_correct(self.DATA_LAYER_TOO_LONG)
        assert page.has_element(AdvertiserSitesPage.locators.SPAN_WITH_TEXT(self.INSIDE_ERR))

    @pytest.mark.parametrize('pixel', [PIXEL_DOMAIN], indirect=True)
    def test_add_event_to_pixel(self, pixel):
        page, pixel = pixel[0], pixel[1]
        page.click(page.PIXEL_SETTINGS(self.PIXEL_DOMAIN))
        page.create_event(self.EVENT_NAME)
        page.select_category()
        page.select_condition()
        page.url_contains(self.URL_CONTAINS)
        page.confirm_creating_event()
        assert page.has_element(AdvertiserSitesPage.locators.SPAN_WITH_TEXT(self.EVENT_NAME))

    @pytest.mark.parametrize('pixel', [PIXEL_DOMAIN], indirect=True)
    def test_auditor_tag(self, pixel):
        page, pixel = pixel[0], pixel[1]
        page.click(page.PIXEL_SETTINGS(self.PIXEL_DOMAIN))
        page.create_and_check_tag(self.AUDITOR_TAG)
        page.reload()
        assert page.has_element(page.DIV_WITH_TEXT(self.AUDITOR_TAG))

    @pytest.mark.skip('skip')
    @pytest.mark.parametrize('pixel', [PIXEL_DOMAIN], indirect=True)
    def test_give_access(self, pixel):
        page, pixel = pixel[0], pixel[1]
        page.click(page.PIXEL_SETTINGS(self.PIXEL_DOMAIN))
        page.create_access(self.USER_TO_ACCESS)
        assert page.has_element(AdvertiserSitesPage.locators.SPAN_WITH_TEXT(self.USER_TO_ACCESS))
        page.revoke_access()
        page.reload()
        assert not page.has_element(page.DIV_WITH_TEXT(self.USER_TO_ACCESS))

@pytest.fixture(scope='function')
def pixel(driver, request):
    pixel_domain = request.param
    driver.get(AdvertiserSitesPage.url)
    page = AdvertiserSitesPage(driver)
    page.add_pixel(pixel_domain)
    yield (page, pixel_domain)
    page.back_to_sites()
    page.dell_pixel(pixel_domain)
    page.reload()