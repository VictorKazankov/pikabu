from pages.basepage import BasePage


class BetterPage(BasePage):
    def open(self):
        self.browser.get(self.url)
        assert "Лучшие" in self.browser.title
