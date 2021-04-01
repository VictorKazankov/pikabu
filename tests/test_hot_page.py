def test_is_dispalayed_icon_login_comments_elements(hot_page):
    assert hot_page.is_displayed_pikabu_icon()
    assert hot_page.is_displayed_login_form()
    assert hot_page.is_displayed_comments_day()


def test_is_absent_data(hot_page):
    hot_page.open_filter_popup()
    assert hot_page.is_displayed_choose_data_element()
