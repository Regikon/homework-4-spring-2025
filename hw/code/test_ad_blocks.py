from base_case import BaseCase, UserType
from test_partner_sites import PartnerSite
from selenium.webdriver.common.keys import Keys

import pytest

from ui.components.cpm_setting import CountryCPM, RegionCPM


class TestAddAdBlock(BaseCase):
    user = UserType.PARTNER

    AD_BLOCK_NAME_LEN_LIMIT = 200
    CORRECT_BLOCK_NAME = "Корректный блок"
    LETTER_GENERAL_LIMIT = "abcde"
    MAX_ALLOWED_CPM = 10000
    LETTER_COUNTRY_CPM: CountryCPM = {
        "region": "Европа",
        "country": "Германия",
        "value": "abcde"
    }
    MORE_THAN_MAX_COUNTRY_CPM: CountryCPM = {
        "region": "Европа",
        "country": "Германия",
        "value": str(MAX_ALLOWED_CPM + 100)
    }
    VALID_CPM_VALUE = 4848
    VALID_COUNTRY_CPM: CountryCPM = {
        "region": "Европа",
        "country": "Германия",
        "value": "1234"
    }
    LETTER_REGION_CPM: RegionCPM = {
        "region": "Европа",
        "value": "abcde"
    }
    MORE_THAN_MAX_REGION_CPM: RegionCPM = {
        "region": "Европа",
        "value": str(MAX_ALLOWED_CPM + 100)
    }
    VALID_REGION_CPM: RegionCPM = {
        "region": "Европа",
        "value": "4567"
    }
    NO_CPM = "CPM не задан"
    NOT_EXISTANT_COUNTRY = "123123123123"

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

    @pytest.mark.skip('skip')
    def test_general_cpm_ignores_if_cpm_is_greater_than_max(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        cpm_value = self.MAX_ALLOWED_CPM + 50
        add_block_page.cpm_settings.set_general_limit(str(cpm_value))
        limit = add_block_page.cpm_settings.general_limit
        assert len(limit) == 0 or float(limit) != cpm_value

    @pytest.mark.skip('skip')
    def test_sets_general_cpm(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.set_general_limit(str(self.VALID_CPM_VALUE))
        assert float(add_block_page.cpm_settings.general_limit) == self.VALID_CPM_VALUE

    @pytest.mark.skip('skip')
    def test_country_cpm_ignores_letters(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.set_country_cpm(self.LETTER_COUNTRY_CPM)
        add_block_page.cpm_settings.toggle_region_dropdown(self.LETTER_COUNTRY_CPM['region'])
        got_cpm = add_block_page.cpm_settings.get_cpm_limit(self.LETTER_COUNTRY_CPM['country'])
        assert got_cpm == self.NO_CPM

    @pytest.mark.skip('skip')
    def test_country_cpm_ignores_if_cpm_is_greater_than_max(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.set_country_cpm(self.MORE_THAN_MAX_COUNTRY_CPM)
        add_block_page.cpm_settings.toggle_region_dropdown(self.MORE_THAN_MAX_COUNTRY_CPM['region'])
        got_cpm = add_block_page.cpm_settings.get_cpm_limit(self.MORE_THAN_MAX_COUNTRY_CPM['country'])
        assert got_cpm == self.NO_CPM or float(got_cpm) != float(self.MORE_THAN_MAX_COUNTRY_CPM['value'])

    @pytest.mark.skip('skip')
    def test_sets_country_cpm(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.set_country_cpm(self.VALID_COUNTRY_CPM)
        add_block_page.cpm_settings.toggle_region_dropdown(self.VALID_COUNTRY_CPM['region'])
        got_cpm = add_block_page.cpm_settings.get_cpm_limit(self.VALID_COUNTRY_CPM['country'])
        assert got_cpm == float(self.VALID_COUNTRY_CPM['value'])

    @pytest.mark.skip('skip')
    def test_region_cpm_ignores_letters(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.set_region_cpm(self.LETTER_REGION_CPM)
        got_cpm = add_block_page.cpm_settings.get_cpm_limit(self.LETTER_REGION_CPM['region'])
        assert got_cpm == self.NO_CPM

    @pytest.mark.skip('skip')
    def test_region_cpm_ignores_if_cpm_is_greater_than_max(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.set_region_cpm(self.MORE_THAN_MAX_REGION_CPM)
        got_cpm = add_block_page.cpm_settings.get_cpm_limit(self.MORE_THAN_MAX_REGION_CPM['region'])
        assert got_cpm == self.NO_CPM or float(got_cpm) != float(self.MORE_THAN_MAX_REGION_CPM['value'])

    @pytest.mark.skip('skip')
    def test_region_country_cpm(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.set_region_cpm(self.VALID_REGION_CPM)
        got_cpm = add_block_page.cpm_settings.get_cpm_limit(self.VALID_REGION_CPM['region'])
        assert float(got_cpm) == float(self.VALID_REGION_CPM['value'])

    @pytest.mark.skip('skip')
    def test_region_cpm_has_lower_priority_than_country(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.set_country_cpm(self.VALID_COUNTRY_CPM)
        add_block_page.cpm_settings.set_region_cpm(self.VALID_REGION_CPM)
        add_block_page.cpm_settings.toggle_region_dropdown(self.VALID_COUNTRY_CPM['region'])
        region_cpm = add_block_page.cpm_settings.get_cpm_limit(self.VALID_REGION_CPM['region'])
        country_cpm = add_block_page.cpm_settings.get_cpm_limit(self.VALID_COUNTRY_CPM['country'])
        assert region_cpm != country_cpm

    @pytest.mark.skip('skip')
    def test_cpm_filters_only_set_values(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.set_region_cpm(self.VALID_REGION_CPM)
        add_block_page.cpm_settings.toggle_show_only_set_cpms()
        assert not add_block_page.cpm_settings.has_no_cpm_values()

    @pytest.mark.skip('skip')
    def test_cpm_search_finds_country(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.search(self.VALID_COUNTRY_CPM['country'])
        assert add_block_page.cpm_settings.has_country_or_region(self.VALID_COUNTRY_CPM['country'])

    @pytest.mark.skip('skip')
    def test_cpm_search_hides_countries_if_not_found(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.search(self.NOT_EXISTANT_COUNTRY)
        assert not add_block_page.cpm_settings.has_any_country()


