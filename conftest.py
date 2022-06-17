
from selene.support.shared import browser
import pytest


@pytest.fixture(scope='session', autouse=True)
def setup():
    browser.config.window_width = 1280
    browser.config.window_height = 720


@pytest.fixture
def open_google():
    browser.open('https://google.com')