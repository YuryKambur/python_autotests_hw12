import os

import pytest
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selene import browser
from utils import allure_attach

DEFAULT_BROWSER_VERSION = "128.0"
DEFAULT_BROWSER_NAME = "chrome"

def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        default='chrome'
    )
    parser.addoption(
        '--browser_version',
        default='128.0'
    )

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def setup_browser(request):
    browser_name = request.config.getoption('--browser_name')
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    if browser_name == "chrome":
        options = ChromeOptions()
        options.set_capability("browserName", "chrome")
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.set_capability("browserName", "firefox")
    options.set_capability("browserName", browser_name)
    options.set_capability("browserVersion", browser_version)
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })

    selenoid_login = os.getenv("LOGIN")
    selenoid_pass = os.getenv("PASSWORD")
    selenoid_url = os.getenv("URL")

    browser.config.driver_remote_url = f"https://{selenoid_login}:{selenoid_pass}{selenoid_url}"
    browser.config.driver_options = options
    browser.config.timeout = 10

    yield browser

    allure_attach.add_screenshot(browser)
    allure_attach.add_logs(browser)
    allure_attach.add_html(browser)
    allure_attach.add_video(browser)

    browser.quit()

