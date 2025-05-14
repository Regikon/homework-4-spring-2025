from base_case import BaseCase, UserType
from test_partner_sites import PartnerSite
from selenium.webdriver.common.keys import Keys

import pytest


class TestAddAdBlock(BaseCase):
    user = UserType.PARTNER

    AD_BLOCK_NAME_LEN_LIMIT = 200
    CORRECT_BLOCK_NAME = "Корректный блок"
    LETTER_GENERAL_LIMIT = "abcde"
    MAX_ALLOWED_CPM = 10000

    @pytest.mark.skip('skip')
    def test_click_to_amp_radiobutton_removes_display_block_format(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.toggle_amp_page()
        assert not add_block_page.has_recommend_widget()
        assert not add_block_page.has_video_instream()
        assert not add_block_page.has_tune_design_button()
        assert not add_block_page.has_integration_type_radiogroup()

    @pytest.mark.skip('skip')
    def test_error_if_name_is_empty(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.set_block_name('a' + Keys.BACKSPACE)
        assert add_block_page.has_name_empty_error()
        assert not add_block_page.create_button_is_enabled()

    @pytest.mark.skip('skip')
    def test_error_if_name_is_too_long(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.set_block_name('a' * (2 * self.AD_BLOCK_NAME_LEN_LIMIT))
        assert add_block_page.has_name_too_long_error()
        assert not add_block_page.create_button_is_enabled()

    @pytest.mark.skip('skip')
    def test_ok_if_entered_correct_name(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.set_block_name(self.CORRECT_BLOCK_NAME)
        assert not add_block_page.has_name_error()

    @pytest.mark.skip('skip')
    def test_no_size_selection_if_recommend_widget(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_recommend_widget_type()
        assert not add_block_page.has_size_selection()

    @pytest.mark.skip('skip')
    def test_general_cpm_ignores_letters(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.set_general_limit(self.LETTER_GENERAL_LIMIT)
        for ch in add_block_page.cpm_settings.general_limit:
            assert not ch.isalpha()

    #@pytest.mark.skip('skip')
    def test_general_cpm_ignores_if_cpm_is_greater_than_max(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        cpm_value = self.MAX_ALLOWED_CPM + 50
        add_block_page.cpm_settings.set_general_limit(str(cpm_value))
        limit = add_block_page.cpm_settings.general_limit
        assert len(limit) == 0 or float(limit) != cpm_value

