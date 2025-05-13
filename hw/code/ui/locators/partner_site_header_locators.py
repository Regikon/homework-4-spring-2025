from selenium.webdriver.common.by import By

class PartnerSiteHeaderLocators:
    # Basically div with defined class contains element with defined class
    SITE_NAME = (By.XPATH, "//div[contains(concat(' ', normalize-space(@class), ' '), 'header_editableTextWrapper')]//*[contains(concat(' ', normalize-space(@class), ' '), 'EditableText_text')]")
    SITE_NAME_INPUT = (By.XPATH, "//div[contains(concat(' ', normalize-space(@class), ' '), 'EditableText_container_editing')]//input")
    SITE_LINK = (By.XPATH, "//div[contains(concat(' ', normalize-space(@class), ' '), 'header_editableTextWrapper')]//a")
    NAME_TOO_LONG_ERROR = (By.XPATH, "//*[contains(concat(' ', normalize-space(@class), ' '), 'header_editableTextError')][contains(., 'Название не должно превышать 200 символов')]")
