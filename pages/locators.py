from selenium.webdriver.common.by import By


class GeneralLocators():
    ICON_SITE = (By.XPATH, "//i[@class='sprite sprite--ui__logo']")
    LOGIN_FORM = (By.XPATH, "//div[@class='tabs sidebar-auth']/parent::*")
    COMMENTS_DAY_BLOG = (By.XPATH, "//div[@class='sidebar-block__content sidebar-comment-day']/parent::*")
    FILTER_BUTTON = (By.XPATH, "//span[@class='button-filter__inner']")
    CHOOSE_DATA = (By.XPATH, "//span[contains(text(),'Выбрать дату')]")


class HotPageLocators():
    pass
