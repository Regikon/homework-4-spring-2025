import pytest
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = ChromeOptions()
    if selenoid:
        options.set_capability('browserName', 'chrome')
        options.set_capability('version', '136.0')
        if vnc:
            options.set_capability('enableVNC', True)

        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options,
        )
    elif browser == 'chrome':
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(options=options, service=service)
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    # This line causes linux webdriver to crash
    # driver.maximize_window()
    yield driver
    driver.quit()

def get_driver(browser_name):
    if browser_name == 'chrome':
        options = ChromeOptions()
        service = ChromeService(executable_path=ChromeDriverManager().install())
        browser = webdriver.Chrome(options=options, service=service)
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')
    return browser

def get_default_driver():
    return get_driver('chrome')

@pytest.fixture(scope='session', params=['chrome'])
def all_drivers(config, request):
    url = config['url']
    browser = get_driver(request.param)
    browser.get(url)
    yield browser
    browser.quit()
