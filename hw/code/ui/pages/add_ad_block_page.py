from ui.components.ad_block_design_settings import AdBlockDesignSettings, BlockDesignSettings
from ui.components.cpm_setting import CPMSettings, CPMSpecification
from ui.locators.add_ad_block_page_locators import AddAdBlockPageLocators
from ui.pages.base_page import BasePage
from utils.re_url import RegExpUrl
from selenium.webdriver.chrome.webdriver import WebDriver
from typing import Literal, Optional, TypedDict, cast
from parse import Result, parse

BlockFormat = Literal["display_block"] | Literal["recommend_widget"] | Literal['amp_display_block']
IntegrationType = Optional[Literal['direct'] | Literal['header_bidding']]
ShowPeriod = Literal['day'] | Literal['week'] | Literal['month']

class AdBlockSettings(TypedDict):
    is_amp: bool
    name: str
    format: BlockFormat
    size: Optional[str]
    design: Optional[BlockDesignSettings]
    integration_type: IntegrationType
    cpm: Optional[CPMSpecification]
    call_code: Optional[str]
    show_limit: int
    period: ShowPeriod
    interval: int

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
        self.set_block_format('recommend_widget')

    def has_size_selection(self):
        self.has_element(self.locators.SIZE_SELECTION_RADIOGROUP, self.FORM_UI_TOGGLING_TIMEOUT)

    def set_size(self, size: str):
        self.click(self.locators.BLOCK_SIZE_OPTION(size))

    def select_manual_cpm(self):
        self.click(self.locators.MANUAL_CPM_RADIOBUTTON)

    def open_design_settings(self) -> AdBlockDesignSettings:
        self.click(self.locators.DESIGN_SETTINGS_BUTTON)
        return AdBlockDesignSettings(self.driver)

    def set_block_format(self, type: BlockFormat):
        if type == 'display_block':
            self.click(self.locators.DISPLAY_BLOCK_OPTION)
        elif type == 'recommend_widget':
            self.click(self.locators.RECOMMEND_WIDGET_OPTION)
        elif type == 'amp_display_block':
            self.click(self.locators.AMP_DISPLAY_BLOCK_OPTION)

    def set_integration_type(self, type: IntegrationType):
        if type is None:
            return
        elif type == 'direct':
            self.click(self.locators.DIRECT_INTEGRATION_RADIOBUTTON)
        elif type == 'header_bidding':
            self.click(self.locators.HEADER_BIDDING_INTEGRATION_RADIOBUTTON)

    def set_call_code(self, code: str):
        input = self.find(self.locators.CALL_CODE_TEXTAREA)
        input.clear()
        input.send_keys(code)

    def set_show_limit(self, limit: int):
        self.click(self.locators.SHOW_LIMIT_SELECT)
        self.click(self.locators.SELECT_OPTION(str(limit) if limit != 0 else "Infinity"))

    def set_show_period(self, period: ShowPeriod):
        self.click(self.locators.SHOW_PERIOD_SELECT)
        self.click(self.locators.SELECT_OPTION(period))

    def set_show_interval(self, interval: int):
        self.click(self.locators.SHOW_INTERVAL_SELECT)
        self.click(self.locators.SELECT_OPTION(str(interval) if interval != 0 else "Infinity"))

    def fill_block_settings(self, settings: AdBlockSettings):
        if settings['is_amp']:
            self.toggle_amp_page()
        self.set_block_name(settings['name'])
        self.set_block_format(settings['format'])
        if settings['size'] is not None:
            self.set_size(settings['size'])
        if settings['design'] is not None:
            design_form = self.open_design_settings()
            design_form.set_design(settings['design'])
            design_form.submit()
        self.set_integration_type(settings['integration_type'])
        if settings['cpm'] is not None:
            self.select_manual_cpm()
            self.cpm_settings.set_cpm(settings['cpm'])
        if settings['call_code'] is not None:
            self.set_call_code(settings['call_code'])
        self.set_show_limit(settings['show_limit'])
        self.set_show_period(settings['period'])
        self.set_show_interval(settings['interval'])

    def submit(self): #TODO: redirect to the block page
        self.click(self.locators.SUBMIT_BUTTON)
