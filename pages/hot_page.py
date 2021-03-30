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
        pass

    pass
