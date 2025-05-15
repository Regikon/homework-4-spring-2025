from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from ui.components.base_component import BaseComponent
from ui.locators.ad_block_header_locators import AdBlockHeaderLocators
from selenium.webdriver.chrome.webdriver import WebDriver


class AdBlockHeader(BaseComponent):
    locators = AdBlockHeaderLocators

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        # This guaranties the header to be loaded
        self.find(self.locators.GET_CODE_BUTTON)

    @property
    def block_name(self):
        return self.find(self.locators.BLOCK_NAME).text

    @property
    def block_format(self):
        return self.find(self.locators.BLOCK_FORMAT).text

    @property
    def block_integration(self):
        return self.find(self.locators.BLOCK_INTEGRATION).text

    def is_name_input_active(self):
        return self.has_element(self.locators.BLOCK_NAME_INPUT)

    def has_name_too_long_error(self):
        return self.has_element(self.locators.NAME_TOO_LONG_ERROR)

    def get_matching_code(self) -> str:
        self.click(self.locators.GET_CODE_BUTTON)
        code = self.find(self.locators.INTEGRATION_CODE).text
        self.click(self.locators.COPY_INTEGRATION_CODE_BUTTON)
        return code

    def set_block_name(self, name: str):
        block_name = self.find(self.locators.BLOCK_NAME)
        ActionChains(self.driver)\
            .click(block_name)\
            .send_keys(name)\
            .send_keys(Keys.RETURN)\
            .perform()
        
