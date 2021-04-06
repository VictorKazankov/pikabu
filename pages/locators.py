from selenium.webdriver.common.by import By


class GeneralLocators():
    ICON_SITE = (By.XPATH, "//i[@class='sprite sprite--ui__logo']")
    LOGIN_FORM = (By.XPATH, "//div[@class='tabs sidebar-auth']/parent::*")
    COMMENTS_DAY_BLOG = (By.XPATH, "//div[@class='sidebar-block__content sidebar-comment-day']/parent::*")
    FILTER_BUTTON = (By.XPATH, "//span[@class='button-filter__inner']")
    CHOOSE_DATA = (By.XPATH, "//span[contains(text(),'Выбрать дату')]")
    BETTER_TAB_LINK = (By.XPATH, "//a[@href='/best']")
    RATINGS_LIST = (By.CLASS_NAME, "story__rating-count")
    CALENDAR_OVERLAY = (By.TAG_NAME, "canvas")
    DATA_FROM_AND_TO_LIST = (By.XPATH, "//input[@placeholder='ДД/ММ/ГГГГ']")
    SUCCESS_BUTTON = (By.XPATH, "//button[contains(text(),'Показать посты')]")
    HINT_DATA_LIST = (By.XPATH, "//time[@class='caption story__datetime hint']")
