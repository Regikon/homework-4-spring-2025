# This is an example test to be sure that selenium properly configured
# It violates PageObject intentionally, do not copy the code

from base_case import BaseCase
import time
import pytest

# Pytest TestCase class MUST start with Test
class TestDummy(BaseCase):
    GOOGLE = 'https://www.google.com/'

    # The same goes for test functions, they also must start with test_
    @pytest.mark.skip('skip')
    def test_dummy(self):
        self.driver.get(self.GOOGLE)
        # this thing is also forbidden, but it is not
        # to be runned test so we are fine
        time.sleep(3)
        assert self.driver.current_url == self.GOOGLE
