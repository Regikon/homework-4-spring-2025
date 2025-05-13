import enum
from ui.locators.partner_sites_page_locators import PartnerSitesPageLocators
from ui.pages.base_page import BasePage
from ui.pages.partner_add_site_page import PartnerAddSitePage
from selenium.webdriver.chrome.webdriver import WebDriver
import time

class SiteStatus(enum.IntEnum):
    ARCHIVED = 1
    STOPPED = 2

class PartnerSitesPage(BasePage):
    url = 'https://ads.vk.com/hq/partner/sites'
    locators = PartnerSitesPageLocators

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        if self.has_element(self.locators.CLEAR_ALL_BUTTON):
            # ads thought that it would be great idea
            # to randomly select filters on sites
            # so we have to make sure that none filters
            # are applied when new page is spawn
            self.click(self.locators.CLEAR_ALL_BUTTON)

    def go_to_add_site_page(self) -> PartnerAddSitePage:
        self.click(self.locators.ADD_SITE_BUTTON)
        return PartnerAddSitePage(self.driver)
    
    def has_site_with_id(self, id: int) -> bool:
        return self.has_element(self.locators.SITE_ENTRY(id))

    def set_site_status(self, id: int, status: SiteStatus):
        self.select_site(id)
        locator = self.get_option_locator_by_status(status)
        self.open_actions_dropdown()
        option = self.find(locator)
        option.click()
        time.sleep(2)

    def select_site(self, id: int):
        checkbox = self.find(self.locators.SITE_CHECKBOX(id))
        if not checkbox.is_selected():
            checkbox.click()

    def open_actions_dropdown(self):
        if self.has_element(self.locators.ARCHIVE_OPTION):
            # already open
            return
        dropdown = self.find(self.locators.ACTIONS_DROPDOWN)
        dropdown.click()

    @classmethod
    def get_option_locator_by_status(cls, status: SiteStatus):
        if status == SiteStatus.ARCHIVED:
            return cls.locators.ARCHIVE_OPTION
        elif status == SiteStatus.STOPPED:
            return cls.locators.STOP_OPTION

    def get_site_status(self, site_id: int) -> SiteStatus:
        site_status_elem = self.find(self.locators.SITE_STATUS(site_id))
        status = site_status_elem.get_attribute('data-status')
        if status == "archived":
            return SiteStatus.ARCHIVED
        elif status == "stopped":
            return SiteStatus.STOPPED
        raise RuntimeError("Unknown status")
