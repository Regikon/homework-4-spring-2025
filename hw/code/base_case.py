from typing import Optional
from _pytest.fixtures import FixtureRequest
import pytest
import enum

from conftest import Session
from ui.pages.main_page import MainPage
from ui.pages.advertiser_overview_page import AdvertiserOverviewPage
from ui.pages.partner_dashboard_page import PartnerDashboardPage
from utils.local_storage import (get_all_local_storage,
    clear_local_storage,
    set_local_storage_item
)
from selenium.webdriver.chrome.webdriver import WebDriver

class UserType(enum.IntEnum):
    ADVERTISER = 1
    PARTNER = 2

class BaseCase:
    driver: WebDriver
    user: Optional[UserType]

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, request: FixtureRequest, driver: WebDriver, config):
        self.driver = driver
        self.config = config

        if self.user is not None:
            # We need to login
            session = self.__extract_session(request)
            if session['cookie'] is None or session['local_storage'] is None:
                user_id = self.__get_user_id(request)
                self.__login(user_id)
                session['cookie'] = self.driver.get_cookies()
                session['local_storage'] = get_all_local_storage(self.driver)
            else:
                for cookie in session['cookie']:
                    self.driver.add_cookie(cookie)
                clear_local_storage(self.driver)
                for key, value in session['local_storage'].items():
                    set_local_storage_item(self.driver, key, value)

        # If you want to add your page, you can do like this
        # self.my_page: MyPage = (request.getfixturevalue('my_page'))
        # request is a FixtureRequest, added as a parameter to this function

    def __login(self, user_id):
        self.driver.get(MainPage.url)
        main_page = MainPage(self.driver)
        login_page = main_page.go_to_login_page()
        undefined_profile_page = login_page.login()
        undefined_profile_page.switch_account(user_id)
        if self.user == UserType.ADVERTISER:
            return AdvertiserOverviewPage(self.driver)
        elif self.user == UserType.PARTNER:
            return PartnerDashboardPage(self.driver)
        return None

    def __extract_session(self, request: FixtureRequest) -> Session:
        if self.user == UserType.ADVERTISER:
            return request.getfixturevalue('advertiser_session')
        return request.getfixturevalue('partner_session')

    def __get_user_id(self, request: FixtureRequest) -> str:
        if self.user == UserType.ADVERTISER:
            return request.getfixturevalue('advertiser_id')
        return request.getfixturevalue('partner_id')
