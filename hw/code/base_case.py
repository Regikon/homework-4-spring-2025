import pytest

from selenium.webdriver.chrome.webdriver import WebDriver
from ui.pages.pre_login_page import PreLoginPage
import time
import json

class BaseCase:
    driver: WebDriver
    User = None
    Cookies_created = False

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver: WebDriver, config):
        self.driver = driver
        self.config = config

        if self.User=="Advertiser":
            if not self.Cookies_created:
                print("Cookies creating...")
                self.pre_login = PreLoginPage(driver)
                self.id_auth = self.pre_login.go_to_login_page()
                time.sleep(10)
                
                self.registration = self.id_auth.go_to_registration_page()

                cookies = driver.get_cookies()
                with open('cookies.json', 'w') as file:
                    json.dump(cookies, file)
                self.Cookies_created = True
            else:
                print("Cookies already created")
                with open('cookies.json', 'r') as file:
                    cookies = json.load(file)
                for cookie in cookies:
                    driver.add_cookie(cookie)
                driver.refresh()
        elif self.User=="Partner":
            pass
        # If you want to add your page, you can do like this
        # self.my_page: MyPage = (request.getfixturevalue('my_page'))
        # request is a FixtureRequest, added as a parameter to this function
