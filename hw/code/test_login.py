from base_case import BaseCase, UserType
from ui.pages.main_page import MainPage
import pytest

class TestLogin(BaseCase):
    user = None

    @pytest.mark.skip('skip')
    def test_login(self):
        self.driver.get(MainPage.url)
        main_page = MainPage(self.driver)
        login_page = main_page.go_to_login_page()
        login_page.login()


class TestPartnerLogin(BaseCase):
    user = UserType.PARTNER

    @pytest.mark.skip('skip')
    def test_has_cookies(self):
        assert len(self.driver.get_cookies()) > 0

    @pytest.mark.skip('skip')
    def test_does_not_need_login_twice(self):
        # If you prompted to login, test failed
        pass
