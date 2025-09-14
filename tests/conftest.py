import pytest
from selene import browser, have



@pytest.fixture(scope='session')
def open_registration_form():
    browser.config.window_width = 1280
    browser.config.window_height = 720
    browser.open("https://demoqa.com/automation-practice-form")
    yield browser
    browser.quit()
