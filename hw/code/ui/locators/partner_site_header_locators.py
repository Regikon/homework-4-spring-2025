from selenium.webdriver.common.by import By

class PartnerSiteHeaderLocators:
    # Basically div with defined class contains element with defined class
    SITE_NAME_INPUT = (By.XPATH, "//div[contains(concat(' ', normalize-space(@class), ' '), 'header_editableTextWrapper')]//*[contains(concat(' ', normalize-space(@class), ' '), 'EditableText_text')]")
    SITE_LINK = (By.XPATH, "//div[contains(concat(' ', normalize-space(@class), ' '), 'header_editableTextWrapper')]//a")
