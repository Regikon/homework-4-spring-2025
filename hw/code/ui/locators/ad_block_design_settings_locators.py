from typing import Literal
from selenium.webdriver.common.by import By

class AdBlockDesignSettingsLocators:
    BLOCK_SCALE_INPUT = (By.XPATH, '//*[contains(@class, BlockDesign_previewControlsInput)][contains(., "%")]/input')

    BLOCK_FRAME_SELECT = (By.XPATH, '//*[contains(@class, BlockDesign_designOptions_)][contains(., "Рамка")]/input')
    BLOCK_FRAME_NONE_OPTION = (By.XPATH, "//div[contains(@id, 'none')]")
    BLOCK_FRAME_SOLID_OPTION = (By.XPATH, "//div[contains(@id, 'solid')]")
    BLOCK_FRAME_COLOR_INPUT = (By.XPATH, '//*[contains(@class, "vkuiFormItem")][contains(., "Цвет рамки")]//input')

    HEADER_COLOR_INPUT = (By.XPATH, '//*[contains(@class, "vkuiFormItem")][contains(., "Цвет заголовка")]//input')
    HEADER_LINK_COLOR_INPUT = (By.XPATH, '//*[contains(@class, "vkuiFormItem")][contains(., "Стиль ссылки")]//input')
    HEADER_FONT_SELECT = (By.XPATH, '//*[@data-rbd-draggable-id="title"]//*[contains(@class, "vkuiFormItem")][contains(., "Шрифт")]//input')

    @staticmethod
    def FONT_OPTION(font: str):
        return (By.XPATH, f"//div[contains(@id, '{font}')]")

    HEADER_LINK_UNDERLINE_SELECT = (By.XPATH, '//*[contains(@class, "vkuiFormItem")][contains(., "Подчёркивание")]//input')

    @staticmethod
    def HEADER_LINK_UNDERLINE_OPTION(opt: Literal['underline'] | Literal['none']):
        return (By.XPATH, f"//div[contains(@id, '{opt}')]")

    TEXT_COLOR_INPUT = (By.XPATH, '//*[@data-rbd-draggable-id="text"]//*[contains(@class, "vkuiFormItem")][contains(., "Цвет текста")]//input')
    TEXT_FONT_SELECT = (By.XPATH, '//*[@data-rbd-draggable-id="text"]//*[contains(@class, "vkuiFormItem")][contains(., "Шрифт")]//input')

    BUTTON_BACKGROUND_COLOR_INPUT = (By.XPATH, '//*[contains(@class, "vkuiFormItem")][contains(., "Цвет фона")]//input')
    BUTTON_TEXT_COLOR_INPUT = (By.XPATH, '//*[@data-rbd-draggable-id="button"]//*[contains(@class, "vkuiFormItem")][contains(., "Цвет текста")]//input')
    BUTTON_FONT_SELECT = (By.XPATH, '//*[@data-rbd-draggable-id="button"]//*[contains(@class, "vkuiFormItem")][contains(., "Шрифт")]//input')

    SUBMIT_BUTTON = (By.XPATH, '//button[contains(., "Применить")]')

    BANNER_PREVIEW_IFRAME = (By.XPATH, '//iframe[@id="vka_preview"]')
    BANNER = (By.TAG_NAME, 'ins')

    SECTION_DROPDOWNS = (By.XPATH, '//div[contains(@id, "react-collapsed-toggle")]')
