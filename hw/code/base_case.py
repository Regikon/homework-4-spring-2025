from typing import Dict, List, Optional
from _pytest.fixtures import FixtureRequest
import pytest
import enum

from ui.pages.main_page import MainPage
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
            if len(session) == 0:
                self.__login()
                session.clear()
                session.extend(self.driver.get_cookies())
                return
            for cookie in session:
                self.driver.add_cookie(cookie)

        # If you want to add your page, you can do like this
        # self.my_page: MyPage = (request.getfixturevalue('my_page'))
        # request is a FixtureRequest, added as a parameter to this function

    def __login(self):
        self.driver.get(MainPage.url)
        main_page = MainPage(self.driver)
        login_page = main_page.go_to_login_page()
        login_page.login()

    def __extract_session(self, request: FixtureRequest) -> List[Dict[str, str]]:
        if self.user == UserType.ADVERTISER:
            return request.getfixturevalue('advertiser_session')
        return request.getfixturevalue('partner_session')

