import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

from pages.better_page import BetterPage
from pages.hot_page import HotPage


# from pages.search_page import SearchPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
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


def change_browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        br = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == "firefox":
        br = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise ValueError("Unrecognized browser {}".format(browser_name))
    return br


@pytest.fixture(scope="session")
def browser(request):
    browser = change_browser(request)
    browser.maximize_window()
    yield browser
    browser.quit()


# @pytest.fixture()
# def hot_page(browser):
#     home_page_url = "https://pikabu.ru/"
#     home_page = HotPage(browser, home_page_url)
#     home_page.open()
#     return home_page


@pytest.fixture()
def better_page(browser, hot_page):
    hot_page.open_better_page()
    better_page = BetterPage(browser, browser.current_url)
    better_page.open()
    return better_page
