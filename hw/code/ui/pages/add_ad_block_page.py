from ui.components.cpm_setting import CPMSettings
from ui.locators.add_ad_block_page_locators import AddAdBlockPageLocators
from ui.pages.base_page import BasePage
from utils.re_url import RegExpUrl
from selenium.webdriver.chrome.webdriver import WebDriver
from typing import cast
from parse import Result, parse


class AddAdBlockPage(BasePage):
    locators = AddAdBlockPageLocators
    url = RegExpUrl("https://ads.vk.com/hq/partner/sites/[0-9]+/blocks$")

    FORM_UI_TOGGLING_TIMEOUT = 0.1
    NAME_TOO_LONG_ERROR = "Название не должно превышать 200 символов"
    NAME_EMPTY_ERROR = "Не может быть пустым"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.cpm_settings = CPMSettings(driver)
        # Sometimes frontend just doesn't select
        # the site, so we make sure that the site
        # is selected manually
        parsed_url = parse("https://ads.vk.com/hq/partner/sites/{site_id}/blocks",
                           self.driver.current_url
        )
        self.__id = int(cast(Result, parsed_url).named['site_id'])
        self.click(self.locators.SITE_SELECT)
        self.click(self.locators.SITE_OPTION(self.__id))

    @staticmethod
    def generate_url(site_id: int):
        return f'https://ads.vk.com/hq/partner/sites/{site_id}/blocks'

    def toggle_amp_page(self):
        # We cannot determine if checkbox is checked because
        # the site does not give us this information
        self.click(self.locators.SITE_IS_AMP_PAGE_CHECKBOX)

    def has_recommend_widget(self) -> bool:
        return self.has_element(self.locators.RECOMMEND_WIDGET_OPTION, self.FORM_UI_TOGGLING_TIMEOUT)

    def has_video_instream(self) -> bool:
        return self.has_element(self.locators.INSTREAM_VIDEO_OPTION, self.FORM_UI_TOGGLING_TIMEOUT)

    def has_tune_design_button(self) -> bool:
        return self.has_element(self.locators.DESIGN_SETTINGS_BUTTON, self.FORM_UI_TOGGLING_TIMEOUT)

    def has_integration_type_radiogroup(self) -> bool:
        return self.has_element(self.locators.DIRECT_INTEGRATION_RADIOBUTTON, self.FORM_UI_TOGGLING_TIMEOUT)

    def set_block_name(self, name: str):
        name_input = self.find(self.locators.AD_BLOCK_NAME_INPUT)
        name_input.clear()
        name_input.send_keys(name)

    def has_name_too_long_error(self) -> bool:
        error = self.find(self.locators.NAME_ERROR)
        return error.text == self.NAME_TOO_LONG_ERROR

    def has_name_empty_error(self) -> bool:
        error = self.find(self.locators.NAME_ERROR)
        return error.text == self.NAME_EMPTY_ERROR

    def has_name_error(self) -> bool:
        return self.has_element(self.locators.NAME_ERROR, self.FORM_UI_TOGGLING_TIMEOUT)

    def create_button_is_enabled(self) -> bool:
        button = self.find(self.locators.SUBMIT_BUTTON)
        return button.is_enabled()

    def select_recommend_widget_type(self):
        self.click(self.locators.RECOMMEND_WIDGET_OPTION)

    def has_size_selection(self):
        self.has_element(self.locators.SIZE_SELECTION_RADIOGROUP, self.FORM_UI_TOGGLING_TIMEOUT)

    def select_manual_cpm(self):
        self.click(self.locators.MANUAL_CPM_RADIOBUTTON)
