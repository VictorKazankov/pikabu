import pytest

from pages.hot_page import HotPage

hot_page_url = "https://pikabu.ru/"


class TestGeneralHotPage:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        hot_page = HotPage(browser, hot_page_url)
        hot_page.open()
        return hot_page

    def test_is_dispalayed_icon_login_comments_elements(self, browser):
        hot_page = HotPage(browser, hot_page_url)
        assert hot_page.is_displayed_pikabu_icon()
        assert hot_page.is_displayed_login_form()
        assert hot_page.is_displayed_comments_day()

    def test_is_absent_data(self, browser):
        hot_page = HotPage(browser, hot_page_url)
        hot_page.open_filter_popup()
        assert hot_page.is_displayed_choose_data_element()

    # class TestFilterPosts:
    # def test_opening_calendar(hot_page):
    #     hot_page.open_filter_popup()
    #     hot_page.hover_to_change_data_label()
    #     hot_page.is_displayed_calendar()
    #
    # def test_posts_sorted_by_desc(hot_page):
    #     hot_page.open_filter_popup()
    #     hot_page.hover_to_change_data_label()
    #     hot_page.set_up_data_in_calendat()
    #     success_button = hot_page.is_displayed_show_posts_button()
    #     hot_page.click_show_posts_button(success_button)
    #     # hot_page.is_displayed_download_animation()
    #     rating_list = hot_page.get_values_rating()
    #     hot_page.post_should_be_sorted_desc(rating_list)
    #
    # def test_present_posts_for_certain_date(hot_page):
    #     hot_page.open_filter_popup()
    #     hot_page.hover_to_change_data_label()
    #     hot_page.set_up_data_in_calendat()
    #     success_button = hot_page.is_displayed_show_posts_button()
    #     hot_page.click_show_posts_button(success_button)
    #     hot_page.posts_should_display_for_certain_date()
    #
    # # class TestFoldPosts:
    # def test_is_displayed_show_in_viewed_posts(hot_page):
    #     hot_page.open_filter_popup()
    #     hot_page.is_displayed_show_text()
    #
    # def test_is_displayed_view_type(hot_page):
    #     hot_page.open_filter_popup()
    #     hot_page.open_view_type_list()
    #     hot_page.all_types_should_be_displayed()
    #
    # @pytest.mark.xfail(reason="Posts aren't folded, after opening them in new tabs")
    # def test_open_three_posts_in_new_separate_tabs(hot_page):
    #     url_posts_list = hot_page.get_list_url_for_all_articles()
    #     # open 3 top posts in new tabs
    #     hot_page.open_post_to_new_tab(url_posts_list[0])
    #     hot_page.open_post_to_new_tab(url_posts_list[1])
    #     hot_page.open_post_to_new_tab(url_posts_list[2])
    #     hot_page.all_new_tabs_should_be_opened()
    #     hot_page.posts_should_be_with_preview()
    #     hot_page.change_fold_type_in_view_panel()
    #     hot_page.three_posts_should_be_folded()
