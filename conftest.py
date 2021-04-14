from threading import Thread

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

from pages.better_page import BetterPage
from pages.hot_page import HotPage

# This array 'caps' defines the capabilities browser, device and OS combinations where the test will run

caps = [{
    'os_version': '10',
    'os': 'Windows',
    'browser': 'chrome',
    'browser_version': 'latest',
    'name': 'Test Chrome',  # test name
    'build': 'Build 1'  # Your tests will be organized within this build
},
    {
        'os_version': '10',
        'os': 'Windows',
        'browser': 'firefox',
        'browser_version': 'latest',
        'name': 'Test Firefox',
        'build': 'Build 1'
    },
    {
        'os_version': '10',
        'os': 'Windows',
        'browser': 'edge',
        'browser_version': '89.0',
        'name': 'Test Edge',
        'build': 'Build 1'
    }]


def change_browser(request):
    driver = webdriver.Remote(
        command_executor='https://victorkazankov1:Sxkc4wihaD9ifsbT2zo9@hub-cloud.browserstack.com/wd/hub',
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
