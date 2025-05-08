import pytest

from selenium.webdriver.chrome.webdriver import WebDriver

class BaseCase:
    driver: WebDriver

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver: WebDriver, config):
        self.driver = driver
        self.config = config

        # If you want to add your page, you can do like this
        # self.my_page: MyPage = (request.getfixturevalue('my_page'))
        # request is a FixtureRequest, added as a parameter to this function
