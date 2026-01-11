import pytest
from pages.github_home_page import GithubHomePageDesktop, GithubHomePageMobile

@pytest.mark.parametrize(
    "page_class, browser, marker",
    [
        (GithubHomePageDesktop, (1920, 1080), "desktop"),
        (GithubHomePageMobile, (375, 812), "mobile"),
    ],
    indirect=["browser"]
)
def test_github_sign_in(page_class, browser, marker, request):
    request.node.add_marker(getattr(pytest.mark, marker))

    page = page_class(browser)
    page.open()
    page.click_sign_in()
    assert "login" in browser.current_url