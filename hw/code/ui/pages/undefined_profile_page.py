from ui.pages.base_page import BasePage
from ui.locators.undefined_profile_page_locators import UndefinedProfilePageLocators

class UndefinedProfilePage(BasePage):
    locators = UndefinedProfilePageLocators
    url = 'https://ads.vk.com/hq/'

    # we need to redefine this method because we have unknown profile
    # and unknown url
    def is_opened(self, timeout=15, starts_with_compare=True) -> bool:
        return super().is_opened(timeout, starts_with_compare)

    def switch_account(self, account_id: str):
        self.click(self.locators.SWITCH_PROFILE_DROPDOWN)
        account = self.find(self.locators.ACCOUNT(account_id))
        account.click()
