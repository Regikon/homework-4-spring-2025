from selenium.webdriver.remote.webelement import WebElement

from ui.locators.advertiser_sites_page_locators import AdvertiserSitesLocators
from .base_page import BasePage

class AdvertiserSites(BasePage):
    locators = AdvertiserSitesLocators
    url = 'https://ads.vk.com/hq/pixels'