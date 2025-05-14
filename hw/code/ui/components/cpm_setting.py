from typing import List, TypedDict
from ui.components.base_component import BaseComponent
from ui.locators.cpm_settings_locators import CPMSettingsLocators

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class CountryCPM(TypedDict):
    region: str
    country: str
    value: int

class RegionCPM(TypedDict):
    region: str
    value: int

class CPMSpecification(TypedDict):
    general_limit: int
    region_cpms: List[RegionCPM]
    country_cpms: List[CountryCPM]


class CPMSettings(BaseComponent):
    locators = CPMSettingsLocators

    MAX_LIMIT_LENGTH = 10

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
    def general_limit(self):
        input = self.find(self.locators.GENERAL_LIMIT_INPUT)
        return input.text

    def set_cpm(self, cpm: CPMSpecification):
        self.set_general_limit(str(cpm['general_limit']))
        for region_cpm in cpm['region_cpms']:
            self.set_region_cpm(region_cpm)
        for country_cpm in cpm['country_cpms']:
            self.set_country_cpm(country_cpm)

    def set_region_cpm(self, cpm: RegionCPM):
        region_dropdown = self.find(self.locators.REGION_DROPDOWN(cpm['region']))
        region_dropdown.click()
        self.set_cpm_limit(cpm['region'], str(cpm['value']))
        region_dropdown.click()

    def set_country_cpm(self, cpm: CountryCPM):
        region_dropdown = self.find(self.locators.REGION_DROPDOWN(cpm['region']))
        region_dropdown.click()
        self.set_cpm_limit(cpm['country'], str(cpm['value']))
        region_dropdown.click()

    def set_cpm_limit(self, region_or_country: str, limit: str):
        input = self.find(self.locators.CPM_INPUT(region_or_country))
        ActionChains(self.driver)\
            .click(input)\
            .send_keys(Keys.BACKSPACE * self.MAX_LIMIT_LENGTH)\
            .send_keys(limit)\
            .send_keys(Keys.RETURN)\
            .perform()
