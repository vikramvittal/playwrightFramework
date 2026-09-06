import pytest

from pages.socialmedia import SocialMedia


@pytest.mark.smoke
def test_social_media_links(page):
    social_media = SocialMedia(page)
    social_media.social_media_page_click()
