import time
from ui.components.base_component import BaseComponent
from ui.locators.mediateka_locators import MediaLoaderLocators

import os

class MediaLoader(BaseComponent):
    locators = MediaLoaderLocators

    def upload_image(self, path):
        file_input = self.find(self.locators.INPUT__LOAD_IMAGE)
        file_input.send_keys(os.path.abspath(path))
        file_input.submit()
    
    def select_image_cat(self):
        self.click(self.locators.IMAGE_CAT_LOGO)
        self.click(self.locators.BUTTON__SAVE, 15)

    def close_modal(self):
        self.click(self.locators.BUTTON__CLOSE)

