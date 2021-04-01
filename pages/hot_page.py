from time import sleep

from pages.basepage import BasePage
from pages.locators import GeneralLocators


class HotPage(BasePage):
    def open(self):
        self.browser.get(self.url)
        assert "Горячее" in self.browser.title
        sleep(1)

    def is_displayed_pikabu_icon(self):
        return self.get_element_present(*GeneralLocators.ICON_SITE)

    def is_displayed_login_form(self):
        return self.get_element_present(*GeneralLocators.LOGIN_FORM)

    def is_displayed_comments_day(self):
        return self.get_element_present(*GeneralLocators.COMMENTS_DAY_BLOG)

    def open_filter_popup(self):
        filter_button = self.get_element_present(*GeneralLocators.FILTER_BUTTON)
        filter_button.click()

    def is_displayed_choose_data_element(self):
        return self.get_element_present(*GeneralLocators.CHOOSE_DATA)
