from time import sleep
from datetime import datetime

from pages.basepage import BasePage
from pages.locators import GeneralLocators


class HotPage(BasePage):
    from_data = '01/02/2021'
    to_data = '10/02/2021'

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

    def open_better_page(self):
        better_tab = self.get_element_present(*GeneralLocators.BETTER_TAB_LINK)
        better_tab.click()

    def hover_to_change_data_label(self):
        self.hover(*GeneralLocators.CHOOSE_DATA)

    def is_displayed_calendar(self):
        assert self.get_element_present(*GeneralLocators.CALENDAR_OVERLAY)

    def set_up_data_in_calendat(self):
        self.hover(*GeneralLocators.CALENDAR_OVERLAY)
        data_from_and_to_list = self.get_elements_present(*GeneralLocators.DATA_FROM_AND_TO_LIST)
        self.set_data_from_and_to_fields_calendar(data_from_and_to_list, self.from_data, self.to_data)

    def is_displayed_show_posts_button(self):
        success_button = self.get_element_present(*GeneralLocators.SUCCESS_BUTTON)
        assert success_button
        return success_button

    def click_show_posts_button(self, success_button):
        success_button.click()
        pass

    def posts_should_display_for_certain_date(self):
        date_list_sorter = self.get_date_list_sorted_from_posts()

        # verify that data last post(top post) = latest choose date in calendar
        data_last_post = datetime.strptime(date_list_sorter[0], '%Y-%m-%d').strftime('%d-%m-%Y')
        data_end = datetime.strptime(self.to_data, '%d/%m/%Y').strftime('%d-%m-%Y')
        assert data_last_post == data_end

        # verify that data first post(bottom post) = first choose date in calendar
        data_first_post = datetime.strptime(date_list_sorter[-1], '%Y-%m-%d').strftime('%d-%m-%Y')
        data_first = datetime.strptime(self.from_data, '%d/%m/%Y').strftime('%d-%m-%Y')
        assert data_first_post == data_first

    def get_date_list_sorted_from_posts(self):
        hint_object_list = self.get_elements_present(*GeneralLocators.HINT_DATA_LIST)
        # get attribute from time hint and cuts time
        data_list = [data.get_attribute("datetime")[:-15] for data in hint_object_list]
        data_list_sorted = sorted(data_list, reverse=True)
        return data_list_sorted

    def is_displayed_show_text(self):
        text_element = self.get_element_present(*GeneralLocators.SHOW_TEXT)
        b = text_element.text
        assert text_element.text == 'показывать'

    def open_view_type_list(self):
        display_mode = self.get_element_present(*GeneralLocators.DISPLAY_MODE_SELECT)
        display_mode.click()

    def all_types_should_be_displayed(self):
        type_objects = self.get_elements_present(*GeneralLocators.DISPLAY_MODE_TYPES)
        types_text = list(map(lambda i: i.text, type_objects))
        correct_types_text = ['показывать', 'сворачивать', 'скрывать']
        assert correct_types_text == types_text

    def get_list_url_for_all_articles(self):
        articles_list = self.get_elements_present(*GeneralLocators.ARTICLES_LIST)
        url_articles_list = list(map(lambda i: i.get_attribute("href"), articles_list))
        return url_articles_list

    def open_article_to_new_tab(self, url):
        self.browser.execute_script(f"window.open('{url}','_blank');")

    def all_new_tabs_should_be_opened(self):
        # count tab = 4(1+3)
        assert len(self.browser.window_handles) == 4
