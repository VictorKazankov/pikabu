import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

from pages.better_page import BetterPage
from pages.hot_page import HotPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--language", action="store", default="ru")


def get_language_local_chrome(request):
    local = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': local})
    return options


def get_language_local_firefox(request):
    local = request.config.getoption("--language")
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", local)
    return fp


caps = [{
  'browserName': 'chrome',
  'browserVersion': '90.0',
  'platformName': 'Windows 10',
  'sauce:options': {
      'screenResolution': '1920x1200'
  }
}, {
  'browserName': 'firefox',
  'browserVersion': '88.0',
  'platformName': 'Windows 10',
  'sauce:options': {
      'screenResolution': '1920x1200'
  }
}, {
  'browserName': 'MicrosoftEdge',
  'browserVersion': '90.0',
  'platformName': 'Windows 10',
  'sauce:options': {
      'screenResolution': '1920x1200'
  }
}
]


def change_browser(request):
    driver = webdriver.Remote(
        command_executor='https://vicprog:63733e7f-b4b3-4c26-9436-f91e0862031a@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
        desired_capabilities=request)
    return driver


@pytest.fixture(scope="session", params=caps, ids=["chrome", "firefox", "edge"])
def browser(request):
    driver = change_browser(request.param)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function", autouse=True)
def hot_page(browser):
    hot_page = HotPage(browser, "https://pikabu.ru/")
    hot_page.open()
    return hot_page


@pytest.fixture(scope="function")
def better_page(browser, hot_page):
    hot_page.open_better_page()
    better_page = BetterPage(browser, browser.current_url)
    better_page.open()
    return better_page