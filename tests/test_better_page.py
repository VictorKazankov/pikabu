class TestPosts:
    def test_posts_sorted(self, better_page):
        rating_list = better_page.get_values_rating()
        better_page.post_should_be_sorted_desc(rating_list)
