import pytest
from selene import browser, have



@pytest.fixture(scope='session')
def open_registration_page():
    browser.config.window_width = 1280
    browser.config.window_height = 720
    browser.config.base_url = 'https://demoqa.com'
    yield browser
    browser.quit()
