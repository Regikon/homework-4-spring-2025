from typing import List
from base_case import BaseCase, UserType
from test_partner_sites import PartnerSite
from selenium.webdriver.common.keys import Keys
import pytest


from ui.components.ad_block_design_settings import BlockDesignSettings
from ui.components.ad_block_header import AdBlockHeader
from ui.components.cpm_setting import CPMSettings, CPMSpecification, CountryCPM, RegionCPM
from ui.entities.ad_block import AdBlock
from ui.entities.ad_block_settings import AdBlockSettings, AdBlockStatus
from ui.pages.add_ad_block_page import AddAdBlockPage
from ui.pages.partner_site_ad_blocks_page import PartnerSiteAdBlocksPage

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
    BANNER_ZOOM = 50
    DISPLAY_BLOCK_DESIGN_SETTINGS: BlockDesignSettings = {
        'frame': {
            'frame': "solid",
            'color': "#ff0000"
        },
        'header': {
            'color': "#00ff00",
            'link_color': "#0000ff",
            'font': "Verdana",
            'link_underline': 'underline'
        },
        'text': {
            'font': "Tahoma",
            'color': '#fffff1',
        },
        'button': {
            'font': 'Arial',
            'background_color': '#00abf1',
            'text_color': '#ff00ff'
        }
    }
    DISPLAY_BLOCK_CPM: CPMSpecification = {
        'general_limit': '20',
        'country_cpms': [{
            'country': 'Танзания',
            'value': '200',
            'region': 'Африка'
        }],
        'region_cpms': [
            {
                'region': 'Европа',
                'value': '10000'
            }
        ]

    }
    DISPLAY_BLOCK_SETTINGS: AdBlockSettings = {
        'is_amp': False,
        'name': 'my first block',
        'format': 'display_block',
        'size': '300x600',
        'design': DISPLAY_BLOCK_DESIGN_SETTINGS,
        'integration_type': 'direct',
        'cpm': DISPLAY_BLOCK_CPM,
        'call_code': 'elelbobo',
        'show_limit': 26,
        'period': 'week',
        'interval': 24
    }
    DISPLAY_BLOCK_RUSSIAN_INTEGRATION_TYPE = "Прямая интеграция"
    AMP_BLOCK_RUSSIAN_INTEGRATION_TYPE = "Прямая интеграция"
    RECOMMEND_WIDGET_RUSSIAN_INTEGRATION_TYPE = "Прямая интеграция"
    RECOMMEND_WIDGET_LABEL = "Рекомендательный виджет"

    AMP_BLOCK_CPM: CPMSpecification = {
        'general_limit': '2',
        'country_cpms': [
            {
                'region': 'Бывший СССР',
                'country': 'Россия',
                'value': '400'
            }
        ],
        'region_cpms': [
            {
                'region': 'Африка',
                'value': '1000',
            }
        ]
    }

    AMP_BLOCK_SETTINGS: AdBlockSettings = {
        'is_amp': True,
        'name': 'my amp block',
        'format': 'amp_display_block',
        'size': '300x250',
        'design': None,
        'integration_type': None,
        'cpm': AMP_BLOCK_CPM,
        'call_code': '',
        'show_limit': 6,
        'period': 'month',
        'interval': 2
    }
    RECOMMEND_WIDGET_SETTINGS: AdBlockSettings = {
        'name': 'Мой рекомендательный виджет',
        'format': 'recommend_widget',
        'cpm': None,
        'show_limit': 0,
        'period': 'day',
        'interval': 0,
        'call_code': None,
        'size': None,
        'design': None,
        'is_amp': False,
        'integration_type': None
    }

    # Time when UI is expected to have been changed
    # Used when waiting an element to disappear from the UI
    UI_TOGGLE_TIMEOUT = 0.1 #s
    NAME_TOO_LONG_ERROR = "Название не должно превышать 200 символов"
    NAME_EMPTY_ERROR = "Не может быть пустым"

    def test_click_to_amp_radiobutton_removes_display_block_format(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.toggle_amp_page()
        assert not add_block_page.has_element(
            AddAdBlockPage.locators.RECOMMEND_WIDGET_OPTION,
            self.UI_TOGGLE_TIMEOUT)
        assert not add_block_page.has_element(
            AddAdBlockPage.locators.INSTREAM_VIDEO_OPTION,
            self.UI_TOGGLE_TIMEOUT)
        assert not add_block_page.has_element(
            AddAdBlockPage.locators.DESIGN_SETTINGS_BUTTON,
            self.UI_TOGGLE_TIMEOUT)
        assert not add_block_page.has_element(
            AddAdBlockPage.locators.DIRECT_INTEGRATION_RADIOBUTTON,
            self.UI_TOGGLE_TIMEOUT)

    def test_error_if_name_is_empty(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.set_block_name('a' + Keys.BACKSPACE)
        assert add_block_page.find(
            AddAdBlockPage.locators.NAME_ERROR).text == self.NAME_EMPTY_ERROR
        assert not add_block_page.find(
            AddAdBlockPage.locators.SUBMIT_BUTTON).is_enabled()

    def test_error_if_name_is_too_long(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.set_block_name('a' * (2 * self.AD_BLOCK_NAME_LEN_LIMIT))
        assert add_block_page.find(
            AddAdBlockPage.locators.NAME_ERROR).text == self.NAME_TOO_LONG_ERROR
        assert not add_block_page.find(
            AddAdBlockPage.locators.SUBMIT_BUTTON).is_enabled()

    def test_ok_if_entered_correct_name(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.set_block_name(self.CORRECT_BLOCK_NAME)
        assert not add_block_page.has_element(AddAdBlockPage.locators.NAME_ERROR,
                                              self.UI_TOGGLE_TIMEOUT)

    def test_no_size_selection_if_recommend_widget(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_recommend_widget_type()
        assert not add_block_page.has_element(
            AddAdBlockPage.locators.SIZE_SELECTION_RADIOGROUP,
            self.UI_TOGGLE_TIMEOUT
        )


    def test_general_cpm_ignores_letters(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.set_general_limit(self.LETTER_GENERAL_LIMIT)
        for ch in add_block_page.cpm_settings.general_limit:
            assert not ch.isalpha()

    def test_general_cpm_ignores_if_cpm_is_greater_than_max(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        cpm_value = self.MAX_ALLOWED_CPM + 50
        add_block_page.cpm_settings.set_general_limit(str(cpm_value))
        limit = add_block_page.cpm_settings.general_limit
        assert len(limit) == 0 or float(limit) != cpm_value

    def test_sets_general_cpm(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.set_general_limit(str(self.VALID_CPM_VALUE))
        assert float(add_block_page.cpm_settings.general_limit) == self.VALID_CPM_VALUE

    def test_country_cpm_ignores_letters(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.set_country_cpm(self.LETTER_COUNTRY_CPM)
        add_block_page.cpm_settings.toggle_region_dropdown(self.LETTER_COUNTRY_CPM['region'])
        got_cpm = add_block_page.cpm_settings.get_cpm_limit(self.LETTER_COUNTRY_CPM['country'])
        assert got_cpm == self.NO_CPM

    def test_country_cpm_ignores_if_cpm_is_greater_than_max(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.set_country_cpm(self.MORE_THAN_MAX_COUNTRY_CPM)
        add_block_page.cpm_settings.toggle_region_dropdown(self.MORE_THAN_MAX_COUNTRY_CPM['region'])
        got_cpm = add_block_page.cpm_settings.get_cpm_limit(self.MORE_THAN_MAX_COUNTRY_CPM['country'])
        assert got_cpm == self.NO_CPM or float(got_cpm) != float(self.MORE_THAN_MAX_COUNTRY_CPM['value'])

    def test_sets_country_cpm(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.set_country_cpm(self.VALID_COUNTRY_CPM)
        add_block_page.cpm_settings.toggle_region_dropdown(self.VALID_COUNTRY_CPM['region'])
        got_cpm = add_block_page.cpm_settings.get_cpm_limit(self.VALID_COUNTRY_CPM['country'])
        assert got_cpm == float(self.VALID_COUNTRY_CPM['value'])

    def test_region_cpm_ignores_letters(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.set_region_cpm(self.LETTER_REGION_CPM)
        got_cpm = add_block_page.cpm_settings.get_cpm_limit(self.LETTER_REGION_CPM['region'])
        assert got_cpm == self.NO_CPM

    def test_region_cpm_ignores_if_cpm_is_greater_than_max(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.set_region_cpm(self.MORE_THAN_MAX_REGION_CPM)
        got_cpm = add_block_page.cpm_settings.get_cpm_limit(self.MORE_THAN_MAX_REGION_CPM['region'])
        assert got_cpm == self.NO_CPM or float(got_cpm) != float(self.MORE_THAN_MAX_REGION_CPM['value'])

    def test_region_country_cpm(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.set_region_cpm(self.VALID_REGION_CPM)
        got_cpm = add_block_page.cpm_settings.get_cpm_limit(self.VALID_REGION_CPM['region'])
        assert float(got_cpm) == float(self.VALID_REGION_CPM['value'])

    def test_region_cpm_has_lower_priority_than_country(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.set_country_cpm(self.VALID_COUNTRY_CPM)
        add_block_page.cpm_settings.set_region_cpm(self.VALID_REGION_CPM)
        add_block_page.cpm_settings.toggle_region_dropdown(self.VALID_COUNTRY_CPM['region'])
        region_cpm = add_block_page.cpm_settings.get_cpm_limit(self.VALID_REGION_CPM['region'])
        country_cpm = add_block_page.cpm_settings.get_cpm_limit(self.VALID_COUNTRY_CPM['country'])
        assert region_cpm != country_cpm

    def test_cpm_filters_only_set_values(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.set_region_cpm(self.VALID_REGION_CPM)
        add_block_page.cpm_settings.toggle_show_only_set_cpms()
        assert not add_block_page.cpm_settings.has_element(
            CPMSettings.locators.NO_CPM_LABEL,
            self.UI_TOGGLE_TIMEOUT
        )

    def test_cpm_search_finds_country(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.search(self.VALID_COUNTRY_CPM['country'])
        assert add_block_page.has_element(
            CPMSettings.locators.CPM_INPUT(self.VALID_COUNTRY_CPM['country']),
            self.UI_TOGGLE_TIMEOUT
        )

    def test_cpm_search_hides_countries_if_not_found(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.select_manual_cpm()
        add_block_page.cpm_settings.search(self.NOT_EXISTANT_COUNTRY)
        assert not add_block_page.cpm_settings.has_element(
            CPMSettings.locators.NO_CPM_LABEL,
            self.UI_TOGGLE_TIMEOUT
        )

    # The test is skipped because
    # we cannot get css zoom value from the driver
    # (or I did not come with a solution)
    #
    # Basically this test should assert that
    # Real element size is equal to the initial element size
    # scaled with given zoom value
    # But selenium get_size method always returns the initial size
    # because when in the browser, the final size of the ad banner 
    # is calculated using css zoom. 
    # Css width and height attributes
    # of the element are always equal to the initial size
    @pytest.mark.skip('skip')
    def test_block_preview_changes_scale(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        design_settings = add_block_page.open_design_settings()
        design_settings.set_scale(self.BANNER_ZOOM)
        assert design_settings.banner_zoom == float(self.BANNER_ZOOM) / 100

    def test_adds_display_block(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.fill_block_settings(self.DISPLAY_BLOCK_SETTINGS)
        block_page = add_block_page.submit()
        assert block_page.header.block_name == self.DISPLAY_BLOCK_SETTINGS['name']
        assert block_page.header.block_integration == self.DISPLAY_BLOCK_RUSSIAN_INTEGRATION_TYPE
        assert block_page.header.block_format == self.DISPLAY_BLOCK_SETTINGS['size']

    def test_adds_amp_display_block(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.fill_block_settings(self.AMP_BLOCK_SETTINGS)
        block_page = add_block_page.submit()
        assert block_page.header.block_name == self.AMP_BLOCK_SETTINGS['name']
        assert block_page.header.block_integration == self.AMP_BLOCK_RUSSIAN_INTEGRATION_TYPE
        assert block_page.header.block_format == self.AMP_BLOCK_SETTINGS['size']

    def test_adds_recommend_widget_block(self, one_site: PartnerSite):
        add_block_page = one_site.go_to_add_block_page(self.driver)
        add_block_page.fill_block_settings(self.RECOMMEND_WIDGET_SETTINGS)
        block_page = add_block_page.submit()
        assert block_page.header.block_name == self.RECOMMEND_WIDGET_SETTINGS['name']
        assert block_page.header.block_integration == self.RECOMMEND_WIDGET_RUSSIAN_INTEGRATION_TYPE
        assert block_page.header.block_format == self.RECOMMEND_WIDGET_LABEL

class TestAdBlocks(BaseCase):
    user = UserType.PARTNER

    UNEXISTANT_BLOCK_NAME = "oyuohasldnv,.znxckl;ghpoashdflknasl;"

    # This does not work since frontend has a bug
    #
    # The frontend ignores changing the status of ad blocks
    # Button clicks correctly, but the status remains "on moderation"
    @pytest.mark.skip('skip')
    def test_block_status_changes(self, one_ad_block: AdBlock):
        self.driver.get(PartnerSiteAdBlocksPage.generate_url(one_ad_block.site_id))
        blocks_page = PartnerSiteAdBlocksPage(self.driver)
        blocks_page.set_block_status(one_ad_block.name, AdBlockStatus.STOPPED)
        self.driver.refresh()
        status = blocks_page.get_block_status(one_ad_block.id)
        assert status == AdBlockStatus.STOPPED

    def test_duplicates_blocks(self, one_ad_block: AdBlock):
        self.driver.get(PartnerSiteAdBlocksPage.generate_url(one_ad_block.site_id))
        blocks_page = PartnerSiteAdBlocksPage(self.driver)
        duplicate_page = blocks_page.duplicate_block(one_ad_block.id)
        duplicate_id = duplicate_page.block_id
        self.driver.get(PartnerSiteAdBlocksPage.generate_url(one_ad_block.site_id))
        blocks_page = PartnerSiteAdBlocksPage(self.driver)
        assert blocks_page.has_element(
            PartnerSiteAdBlocksPage.locators.BLOCK_ENTRY(duplicate_id))

    # This does not work since frontend has a bug
    #
    # When we click on apply filter button
    # The site with some probability
    # shows that it has applied the filter
    # but in fact it has not.
    @pytest.mark.skip('skip')
    def test_block_list_filters_stopped_sites(self, two_ad_blocks: List[AdBlock]):
        self.driver.get(PartnerSiteAdBlocksPage.generate_url(two_ad_blocks[0].site_id))
        blocks_page = PartnerSiteAdBlocksPage(self.driver)
        first = two_ad_blocks[0]
        second = two_ad_blocks[1]
        blocks_page.set_block_status(first.name, AdBlockStatus.STOPPED)
        blocks_page.apply_filter(AdBlockStatus.STOPPED)
        assert blocks_page.has_element(
            PartnerSiteAdBlocksPage.locators.BLOCK_ENTRY(first.id))
        assert not blocks_page.has_element(
            PartnerSiteAdBlocksPage.locators.BLOCK_ENTRY(second.id))
        assert blocks_page.has_element(
            PartnerSiteAdBlocksPage.locators.ANY_ARCHIVED_BLOCK)

    def test_block_search_finds_block(self, two_ad_blocks: List[AdBlock]):
        self.driver.get(PartnerSiteAdBlocksPage.generate_url(two_ad_blocks[0].site_id))
        blocks_page = PartnerSiteAdBlocksPage(self.driver)
        first = two_ad_blocks[0]
        second = two_ad_blocks[1]
        blocks_page.search(first.name)
        blocks_page.wait_to_block_to_disappear(second.id)
        assert blocks_page.has_element(
            PartnerSiteAdBlocksPage.locators.BLOCK_ENTRY(first.id))
        assert not blocks_page.has_element(
            PartnerSiteAdBlocksPage.locators.BLOCK_ENTRY(second.id))

    def test_block_search_shows_nothing_found_if_nothing_found(self, one_site: PartnerSite):
        blocks_page = one_site.go_to_site_page(self.driver)
        blocks_page.search(self.UNEXISTANT_BLOCK_NAME)
        assert blocks_page.has_element(
            PartnerSiteAdBlocksPage.locators.NOTHING_FOUND_CAPTION)

class TestAdBlock(BaseCase):
    user = UserType.PARTNER

    VALID_BLOCK_NAME = "new name"
    VALID_BLOCK_NAME_MAX_SYMBOLS_COUNT = 200

    def test_block_changes_name(self, one_ad_block: AdBlock):
        block_page = one_ad_block.go_to_block_page(self.driver)
        block_page.header.set_block_name(self.VALID_BLOCK_NAME)
        self.driver.refresh()
        assert block_page.header.block_name == self.VALID_BLOCK_NAME

    def test_block_cannot_change_to_empty_name(self, one_ad_block: AdBlock):
        block_page = one_ad_block.go_to_block_page(self.driver)
        block_page.header.set_block_name('a' + Keys.BACKSPACE)
        assert block_page.header.has_element(
            AdBlockHeader.locators.BLOCK_NAME_INPUT)

    def test_error_if_try_to_set_too_long_site_name(self, one_ad_block: AdBlock):
        block_page = one_ad_block.go_to_block_page(self.driver)
        block_page.header.set_block_name('a' * (2 * self.VALID_BLOCK_NAME_MAX_SYMBOLS_COUNT))
        assert block_page.header.has_element(
            AdBlockHeader.locators.NAME_TOO_LONG_ERROR)

    def test_can_get_matching_code(self, one_ad_block: AdBlock):
        block_page = one_ad_block.go_to_block_page(self.driver)
        code = block_page.header.get_matching_code()
        assert code.find("<script>") >= 0

