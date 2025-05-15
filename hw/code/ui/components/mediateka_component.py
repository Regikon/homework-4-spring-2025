import time
from ui.components.base_component import BaseComponent
from ui.locators.mediateka_locators import MediaLoaderLocators

import os

class MediaLoader(BaseComponent):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MediaLoaderLocators()

    def upload_image(self, path):
        file_input = self.find(self.locators.INPUT__LOAD_IMAGE)
        file_input.send_keys(os.path.abspath(path))
        file_input.submit()
        
    
    def select_image(self, name):
        image_locator = self.locators.image(name)
        self.click(image_locator)
        time.sleep(3) # it's really necessary
        self.click(self.locators.BUTTON__SAVE)

    def close_modal(self):
        self.click(self.locators.BUTTON__CLOSE)

