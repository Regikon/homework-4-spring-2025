from typing import List, TypedDict, cast
from ui.components.base_component import BaseComponent
from ui.locators.cpm_settings_locators import CPMSettingsLocators

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class CountryCPM(TypedDict):
    region: str
    country: str
    value: str

class RegionCPM(TypedDict):
    region: str
    value: str

class CPMSpecification(TypedDict):
    general_limit: str
    region_cpms: List[RegionCPM]
    country_cpms: List[CountryCPM]


class CPMSettings(BaseComponent):
    locators = CPMSettingsLocators

    MAX_LIMIT_LENGTH = 10
    NO_CPM = "CPM не задан"
    UI_UPDATE_TIMEOUT = 1

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def set_general_limit(self, limit: str):
        input = self.find(self.locators.GENERAL_LIMIT_INPUT)
        ActionChains(self.driver)\
            .click(input)\
            .send_keys(Keys.BACKSPACE * self.MAX_LIMIT_LENGTH)\
            .send_keys(limit)\
            .send_keys(Keys.RETURN)\
            .perform()

    @property
    def general_limit(self) -> str:
        input = self.find(self.locators.GENERAL_LIMIT_INPUT)
        return cast(str, input.get_attribute('value'))

    def get_cpm_limit(self, country_or_region: str) -> str:
        self.click(self.locators.CPM_INPUT(country_or_region))
        input = self.find(self.locators.CPM_INPUT_FIELD(country_or_region))
        value = float(cast(str, input.get_attribute('value')))
        input.send_keys(Keys.RETURN)
        return str(value) if value > 0 else self.NO_CPM

    def toggle_region_dropdown(self, region: str):
        self.click(self.locators.REGION_DROPDOWN(region))

    def set_cpm(self, cpm: CPMSpecification):
        self.set_general_limit(cpm['general_limit'])
        for region_cpm in cpm['region_cpms']:
            self.set_region_cpm(region_cpm)
        for country_cpm in cpm['country_cpms']:
            self.set_country_cpm(country_cpm)

    def set_region_cpm(self, cpm: RegionCPM):
        region_dropdown = self.find(self.locators.REGION_DROPDOWN(cpm['region']))
        region_dropdown.click()
        self.set_cpm_limit(cpm['region'], cpm['value'])
        region_dropdown.click()

    def set_country_cpm(self, cpm: CountryCPM):
        region_dropdown = self.find(self.locators.REGION_DROPDOWN(cpm['region']))
        region_dropdown.click()
        self.set_cpm_limit(cpm['country'], cpm['value'])
        region_dropdown.click()

    def set_cpm_limit(self, region_or_country: str, limit: str):
        input = self.find(self.locators.CPM_INPUT(region_or_country))
        ActionChains(self.driver)\
            .click(input)\
            .send_keys(Keys.BACKSPACE * self.MAX_LIMIT_LENGTH)\
            .send_keys(limit)\
            .send_keys(Keys.RETURN)\
            .perform()

    def search(self, query: str):
        input = self.find(self.locators.SEARCH_INPUT)
        input.clear()
        input.send_keys(query)

    def toggle_show_only_set_cpms(self):
        self.click(self.locators.ONLY_SET_CPMS_CHECKBOX)
