from ui.pages.base_page import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver
from ui.locators.companies_page_locators import CompaniesPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class CompaniesPage(BasePage):
    locators = CompaniesPageLocators
    url = "https://ads.vk.com/hq/dashboard/"
    out_url = "https://ads.vk.com/hq/overview"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver.set_window_size(2220, 1480)
    
    def is_opened(self, timeout=15, starts_with_compare=True) -> bool:
        return super().is_opened(timeout, starts_with_compare)

    def create_campaign(self):
        if self.has_element(self.locators.CLOSE_SOME_ADS):
            self.click(self.locators.CLOSE_SOME_ADS)
        if self.has_element(self.locators.CREATE_CAMPAIGN_BUTTON_ALT):
            self.click(self.locators.CREATE_CAMPAIGN_BUTTON_ALT)
        else:
            self.click(self.locators.CREATE_CAMPAIGN_BUTTON)

    def choose_site(self, url: str):
        self.click(self.locators.CHOOSE_SITE_BUTTON)
        url_input = self.find(self.locators.ADVERTISING_SITE_URL_INPUT)
        url_input.send_keys(url)
        url_input.send_keys(Keys.ENTER)

    def choose_budget(self, price: str):
        price_input = self.find(self.locators.PRICE_INPUT)
        price_input.send_keys(price)
        price_input.send_keys(Keys.ENTER)

    def confirm_company(self, price, first=True):
        if first:
            self.wait_clickability(self.locators.WAIT_FOR_ERROR_DIV)
            self.wait_invisibility(self.locators.WAIT_FOR_ERROR_DIV)
        self.click(self.locators.CONTINUE_BUTTON)

    def remove_company(self):
        self.driver.get(self.out_url)
        if self.has_element(self.locators.DELETE_COMPANY):
            self.click(self.locators.DELETE_COMPANY)

    def choose_interests1(self, one_interest: str):
        self.click(self.locators.INTERESTS_AND_BEHAVIOR_DIV)
        self.click(self.locators.INTERESTS_DIV)
        self.click(self.locators.INTEREST_INPUT_MENU)
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.locators.ONE_INTEREST(one_interest))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def rename_any(self, new_name: str):
        self.click(self.locators.EDIT_MAIN_NAME)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.locators.EDIT_MAIN_NAME_INPUT)
        )
        site_name = self.find(self.locators.EDIT_MAIN_NAME_INPUT)
        ActionChains(self.driver)\
            .click(site_name)\
            .send_keys(new_name)\
            .send_keys(Keys.RETURN)\
            .perform()

    def create_minimum_company_settings(self, url: str, price: str):
        self.create_campaign()
        self.choose_site(url)
        self.choose_budget(price)
        self.confirm_company(price)

    def create_minimum_group_settings(self, url: str, price: str, region: str, interest: str, group_name: str):
        self.create_minimum_company_settings(url, price)
        self.region_choose(region)
        self.choose_interests(interest)

    def reload(self):
        ActionChains(self.driver).send_keys(Keys.F5).perform()

    def region_choose1(self, region: str):
        region_input = self.find(self.locators.REGION_INPUT)
        region_input.send_keys(region)  
        self.click(self.locators.REGION_CHECKBOX(region))


    def delete_any(self, chapter_name: str):
        self.click(self.locators.SHOW_DELETE_BUTTON(chapter_name))
        self.click(self.locators.DELL_CHAPTER_BUTTON)
        self.click(self.locators.CONFIRM_DELETE_BUTTON)
        self.wait_invisibility(self.locators.WAIT_FOR_DELETE)

    def wait_clickability(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_invisibility(self, locator, timeout=15):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))
    
    def choose_interests(self, one_interest: str):
        self.click(self.locators.INTERESTS_AND_BEHAVIOR_DIV)
        self.click(self.locators.INTERESTS_DIV)
        self.click(self.locators.INTEREST_INPUT_MENU)

        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.locators.ONE_INTEREST(one_interest))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def region_choose(self, region: str):
        region_input = self.find(self.locators.REGION_INPUT)

        ActionChains(self.driver)\
            .click(region_input)\
            .send_keys(region)\
            .perform()
        WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located(self.locators.REGION_CHECKBOX(region))
        )
        checkbox = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.locators.REGION_CHECKBOX(region))
        )
        ActionChains(self.driver).move_to_element(checkbox).click().perform()

    