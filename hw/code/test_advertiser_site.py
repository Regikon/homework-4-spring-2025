from base_case import BaseCase
import pytest
import time

class TestAdvertiserSites(BaseCase):
    Url = 'https://ads.vk.com/hq/pixels'
    User = "Advertiser"

    #@pytest.mark.skip('skip')
    def test_some(self):
        self.advertiser_sites = self.registration.go_to_advertiser_sites_page()
        add_pixel_button = self.advertiser_sites.find(self.advertiser_sites.locators.ADD_PIXEL)
        assert add_pixel_button != None
    
    #@pytest.mark.skip('skip')
    def test_some2(self):
        self.advertiser_sites = self.registration.go_to_advertiser_sites_page()
        add_pixel_button = self.advertiser_sites.find(self.advertiser_sites.locators.ADD_PIXEL)
        assert add_pixel_button != None
