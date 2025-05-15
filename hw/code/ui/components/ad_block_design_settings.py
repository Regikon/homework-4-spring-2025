from typing import Literal, TypedDict
from ui.components.base_component import BaseComponent
from ui.locators.ad_block_design_settings_locators import AdBlockDesignSettingsLocators
from selenium.webdriver.chrome.webdriver import WebDriver

class BlockFrameSettings(TypedDict):
    frame: Literal['solid'] | Literal['none']
    color: str

class BlockHeaderSettings(TypedDict):
    color: str
    link_color: str
    font: str
    link_underline: Literal['underline'] | Literal['none']

class BlockTextSettings(TypedDict):
    color: str
    font: str

class BlockButtonSettings(TypedDict):
    background_color: str
    text_color: str
    font: str


class BlockDesignSettings(TypedDict):
    frame: BlockFrameSettings
    header: BlockHeaderSettings
    text: BlockTextSettings
    button: BlockButtonSettings

class AdBlockDesignSettings(BaseComponent):
    locators = AdBlockDesignSettingsLocators

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        # Opening all the menus before any other manipulations
        dropdowns = self.find_all(self.locators.SECTION_DROPDOWNS)
        for dropdown in reversed(dropdowns):
            dropdown.click()
        

    def set_scale(self, zoom: int):
        input = self.find(self.locators.BLOCK_SCALE_INPUT)
        input.clear()
        input.send_keys(str(zoom))

    @property
    def banner_zoom(self) -> float:
        self.driver.switch_to.frame(self.find(self.locators.BANNER_PREVIEW_IFRAME))
        banner = self.find(self.locators.BANNER)
        zoom = banner.value_of_css_property('zoom')
        self.driver.switch_to.default_content()
        return float(zoom)

    def set_block_frame(self, frame_settings: BlockFrameSettings):
        self.click(self.locators.BLOCK_FRAME_SELECT)
        if frame_settings['frame'] == 'solid':
            self.click(self.locators.BLOCK_FRAME_SOLID_OPTION)
        elif frame_settings['frame'] == 'none':
            self.click(self.locators.BLOCK_FRAME_NONE_OPTION)
        color_input = self.find(self.locators.BLOCK_FRAME_COLOR_INPUT)
        color_input.clear()
        color_input.send_keys(frame_settings['color'])

    def set_header(self, header_settings: BlockHeaderSettings):
        header_color_input = self.find(self.locators.HEADER_COLOR_INPUT)
        header_color_input.clear()
        header_color_input.send_keys(header_settings['color'])

        link_color_input = self.find(self.locators.HEADER_LINK_COLOR_INPUT)
        link_color_input.clear()
        link_color_input.send_keys(header_settings['link_color'])

        self.click(self.locators.HEADER_FONT_SELECT)
        self.click(self.locators.FONT_OPTION(header_settings['font']))

        self.click(self.locators.HEADER_LINK_UNDERLINE_SELECT)
        self.click(self.locators.HEADER_LINK_UNDERLINE_OPTION(header_settings['link_underline']))

    def set_text(self, text_settings: BlockTextSettings):
        color = self.find(self.locators.TEXT_COLOR_INPUT)
        color.clear()
        color.send_keys(text_settings['color'])

        self.click(self.locators.TEXT_FONT_SELECT)
        self.click(self.locators.FONT_OPTION(text_settings['font']))

    def set_button(self, button_settings: BlockButtonSettings):
        background_color = self.find(self.locators.BUTTON_BACKGROUND_COLOR_INPUT)
        background_color.clear()
        background_color.send_keys(button_settings['background_color'])

        color = self.find(self.locators.BUTTON_TEXT_COLOR_INPUT)
        color.clear()
        color.send_keys(button_settings['text_color'])

        self.click(self.locators.BUTTON_FONT_SELECT)
        self.click(self.locators.FONT_OPTION(button_settings['font']))

    def set_design(self, design: BlockDesignSettings):
        self.set_block_frame(design['frame'])
        self.set_header(design['header'])
        self.set_text(design['text'])
        self.set_button(design['button'])

    def submit(self):
        self.click(self.locators.SUBMIT_BUTTON)
