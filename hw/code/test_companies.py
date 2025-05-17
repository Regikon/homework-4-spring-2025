from base_case import BaseCase, UserType
from ui.pages.companies_page import CompaniesPage
import pytest
import time

class TestAdvertiserSites(BaseCase):
    user = UserType.ADVERTISER
    SITE = "https://uart.site/"
    COMPANY_NAME = "Unique_part_of COMPANY_NAME _site_need_here"
    GROUP_NAME = "Unique_part_of GROUP_NAME _site_need_here"
    ANNOUNCEMENT_NAME = "Unique_part_of ANNOUNCEMENT_NAME _site_need_here"
    WRONG_SITE = "1"
    WRONG_BUDGET = "1"
    OK_BUDGET = "200"
    REGION = "Чувашская Республика"
    INTEREST = "Авто внедорожники"
    UI_TOGGLE_TIMEOUT = 0.1

    def test_create_campaign(self):
        self.driver.get(CompaniesPage.url)
        page = CompaniesPage(self.driver)
        page.create_campaign()
        assert page.has_element(CompaniesPage.locators.CHOOSE_SITE_BUTTON)

    def test_rename_campaign(self):
        self.driver.get(CompaniesPage.url)
        page = CompaniesPage(self.driver)
        page.create_campaign()
        page.rename_any(self.COMPANY_NAME)
        page.reload()
        assert page.has_element(CompaniesPage.locators.COMPANY_NAME(self.COMPANY_NAME),
            self.UI_TOGGLE_TIMEOUT)
    
    def test_wrong_site(self):
        self.driver.get(CompaniesPage.url)
        page = CompaniesPage(self.driver)
        page.create_campaign()
        page.choose_site(self.WRONG_SITE)
        assert page.has_element(CompaniesPage.locators.INVALID_SITE_LINK_ERROR)
    
    def test_wrong_budget(self):
        self.driver.get(CompaniesPage.url)
        page = CompaniesPage(self.driver)
        page.create_campaign()
        page.choose_site(self.SITE)
        page.choose_budget(self.WRONG_BUDGET)
        page.confirm_company(self.WRONG_BUDGET)
        assert page.has_element(CompaniesPage.locators.INVALID_BUDGET_ERROR)
    
    def test_ok_budget_and_site(self):
        self.driver.get(CompaniesPage.url)
        page = CompaniesPage(self.driver)
        page.create_campaign()
        page.choose_site(self.SITE)
        page.choose_budget(self.OK_BUDGET)
        page.confirm_company(self.OK_BUDGET)
        assert not page.has_element(CompaniesPage.locators.INVALID_BUDGET_ERROR)

    @pytest.mark.parametrize('second_chapter_settings', [(SITE, OK_BUDGET, GROUP_NAME)], indirect=True)
    def test_rename_group(self, second_chapter_settings):
        page = second_chapter_settings
        page.choose_interests(self.INTEREST)
        page.rename_any(self.GROUP_NAME)
        page.reload()
        assert page.has_element(self.locators.COMPANY_NAME(self.GROUP_NAME),
            self.UI_TOGGLE_TIMEOUT)

    @pytest.mark.parametrize('second_chapter_settings', [(SITE, OK_BUDGET, GROUP_NAME)], indirect=True)
    def test_region_in_group(self, second_chapter_settings):
        page = second_chapter_settings
        page.choose_interests(self.INTEREST)
        page.rename_any(self.GROUP_NAME)
        page.region_choose(self.REGION)
        assert page.has_element(CompaniesPage.locators.REGION_CHECKBOX(self.REGION))

    @pytest.mark.parametrize('second_chapter_settings', [(SITE, OK_BUDGET, GROUP_NAME)], indirect=True)
    def test_interests_in_group(self, second_chapter_settings):
        page = second_chapter_settings
        page.choose_interests(self.INTEREST)
        page.rename_any(self.GROUP_NAME)
        assert page.has_element(CompaniesPage.locators.SPAN_TEXT(self.INTEREST))

    @pytest.mark.parametrize('third_chapter_settings', [(SITE, OK_BUDGET, ANNOUNCEMENT_NAME, REGION, INTEREST)], indirect=True)
    def test_announcement_rename(self, third_chapter_settings):
        page = third_chapter_settings
        page.rename_any(self.ANNOUNCEMENT_NAME)
        page.reload()
        assert page.has_element(self.locators.COMPANY_NAME(self.ANNOUNCEMENT_NAME),
            self.UI_TOGGLE_TIMEOUT)

@pytest.fixture(scope='function')
def second_chapter_settings(driver, request):
    params = request.param
    url, budget, group_name = params[0], params[1], params[2]
    driver.get(CompaniesPage.url)
    page = CompaniesPage(driver)
    page.create_minimum_company_settings(url, budget)
    yield page
    page.remove_company()

@pytest.fixture(scope='function')
def third_chapter_settings(driver, request):
    params = request.param
    url, budget, group_name, region, interest = announcement_name = params[0], params[1], params[2], params[3], params[4]
    driver.get(CompaniesPage.url)
    page = CompaniesPage(driver)
    page.create_minimum_group_settings(url, budget, region, interest, group_name)
    yield page
    page.remove_company()