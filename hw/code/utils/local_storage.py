from selenium.webdriver.chrome.webdriver import WebDriver

def get_all_local_storage(driver: WebDriver):
    return driver.execute_script("return Object.assign({}, window.localStorage);")

def clear_local_storage(driver: WebDriver):
    return driver.execute_script("window.localStorage.clear();")

def set_local_storage_item(driver: WebDriver, key: str, value: str):
    driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")
