import pytest


def test_is_dispalayed_icon_login_comments_elements(hot_page):
    assert hot_page.is_displayed_pikabu_icon()
    assert hot_page.is_displayed_login_form()
    assert hot_page.is_displayed_comments_day()


def test_is_absent_data(hot_page):
    hot_page.open_filter_popup()
    assert hot_page.is_displayed_choose_data_element()


def test_opening_calendar(hot_page):
    hot_page.open_filter_popup()
    hot_page.hover_to_change_data_label()
    hot_page.is_displayed_calendar()


@pytest.mark.xfail(reason="Sorting function works incorrect")
def test_posts_sorted_by_desc(hot_page):
    hot_page.open_filter_popup()
    hot_page.hover_to_change_data_label()
    hot_page.set_up_data_in_calendat()
    success_button = hot_page.is_displayed_show_posts_button()
    hot_page.click_show_posts_button(success_button)
    # hot_page.is_displayed_download_animation()
    rating_list = hot_page.get_values_rating()
    hot_page.post_should_be_sorted_desc(rating_list)


def test_present_posts_for_certain_date(hot_page):
    hot_page.open_filter_popup()
    hot_page.hover_to_change_data_label()
    hot_page.set_up_data_in_calendat()
    success_button = hot_page.is_displayed_show_posts_button()
    hot_page.click_show_posts_button(success_button)
    hot_page.posts_should_display_for_certain_date()


def test_is_displayed_show_in_viewed_posts(hot_page):
    hot_page.open_filter_popup()
    hot_page.is_displayed_show_text()


def test_is_displayed_view_type(hot_page):
    hot_page.open_filter_popup()
    hot_page.open_view_type_list()
    hot_page.all_types_should_be_displayed()
