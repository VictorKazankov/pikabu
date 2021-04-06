from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from pages.locators import GeneralLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def get_element_present(self, how, what):
        try:
            element = self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return element

    def get_elements_present(self, how, what):
        try:
            elements = self.browser.find_elements(how, what)
        except NoSuchElementException:
            return False
        return elements

    def hover(self, how, what):
        try:
            element = self.browser.find_element(how, what)
            hover = ActionChains(self.browser).move_to_element(element)
            hover.perform()
        except NoSuchElementException:
            return False
        return True

    def set_data_from_and_to_fields_calendar(self, fields_list, from_value, to_value):
        self.add_vulue_to_field(fields_list[0], from_value)
        self.add_vulue_to_field(fields_list[1], to_value)

    def add_vulue_to_field(self, field, value):
        field.click()
        field.clear()
        field.send_keys(value)

    def get_values_rating(self):
        rating_objects = self.get_elements_present(*GeneralLocators.RATINGS_LIST)
        rating_values = list(map(lambda i: int(i.text), rating_objects))
        return rating_values

    def post_should_be_sorted_desc(self, rating_list):
        assert rating_list == sorted(rating_list, reverse=True)
