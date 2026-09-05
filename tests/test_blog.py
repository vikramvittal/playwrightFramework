import pytest

from pages.blog import Blog


@pytest.mark.smoke
def test_blog_navigation(page):
    blog = Blog(page)
    blog.blog_navigation()
