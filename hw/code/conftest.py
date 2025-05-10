from typing import Dict, List, Tuple
from ui.fixtures import *
import pytest
import dotenv
import os

def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='https://ads.vk.com')
    parser.addoption('--debug_log', action='store_true')
    parser.addoption('--selenoid', action='store_true')
    parser.addoption('--vnc', action='store_true')

@pytest.fixture(scope='session')
def config(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')
    debug_log = request.config.getoption('--debug_log')
    if request.config.getoption('--selenoid'):
        if request.config.getoption('--vnc'):
            vnc = True
        else:
            vnc = False
        selenoid = 'http://127.0.0.1:4444/wd/hub'
    else:
        selenoid = None
        vnc = False

    dotenv.load_dotenv()

    return {
        'browser': browser,
        'url': url,
        'debug_log': debug_log,
        'selenoid': selenoid,
        'vnc': vnc,
    }

@pytest.fixture(scope='session')
def partner_credentials() -> Tuple[str, str]:
    user = os.getenv("FSO_PARTNER_USER")
    if user is None:
        raise RuntimeError("partner user is not provided via FSO_PARTNER_USER variable")
    password = os.getenv("FSO_PARTNER_PASSWORD")
    if password is None:
        raise RuntimeError("partner password is not provided via FSO_PARTNER_PASSWORD variable")
    return (
        user,
        password
    )

@pytest.fixture(scope='session')
def partner_id() -> str:
    id = os.getenv("FSO_PARTNER_ID")
    if id is None:
        raise RuntimeError("partner id is requested, but not found in FSO_PARTNER_ID env variable")
    return id

@pytest.fixture(scope='session')
def advertiser_id() -> str:
    id = os.getenv("FSO_ADVERTISER_ID")
    if id is None:
        raise RuntimeError("partner id is requested, but not found in FSO_ADVERTISER_ID env variable")
    return id


@pytest.fixture(scope='session')
def advertiser_credentials() -> Tuple[str, str]:
    user = os.getenv("FSO_ADVERTISER_USER")
    if user is None:
        raise RuntimeError("advertiser user is not provided via FSO_ADVERTISER_USER variable")
    password = os.getenv("FSO_ADVERTISER_PASSWORD")
    if password is None:
        raise RuntimeError("partner password is not provided via FSO_ADVERTISER_PASSWORD variable")
    return (
        user,
        password
    )

@pytest.fixture(scope='session')
def partner_session() -> List[Dict[str, str]]:
    # Login code is responsible for filling this list
    return []

@pytest.fixture(scope='session')
def advertiser_session() -> List[Dict[str, str]]:
    # Login code is responsible for filling this list
    return []
