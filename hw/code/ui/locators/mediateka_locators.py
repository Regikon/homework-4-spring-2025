from selenium.webdriver.common.by import By

class MediaLoaderLocators:
    BUTTON__CLOSE = (
        By.XPATH,
        "//div[contains(@class, 'ModalRoot')][contains(., 'Медиатека')]//button[@aria-label='Close']"
    )
    INPUT__LOAD_IMAGE = (
        By.XPATH,
        "//div[contains(@class, 'LocalFileSelector_topContent')]//input"
    )
    IMAGE_CAT_LOGO = (
        By.XPATH,
        "//div[contains(@class, 'ImageItem_imageItem')][.//span[text()='logo.jpg']]"
    )
    BUTTON__SAVE = (
        By.XPATH,
        "//button[.//span[contains(text(), 'Сохранить')]]"
    )
