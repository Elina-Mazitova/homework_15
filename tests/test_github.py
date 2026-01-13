import pytest
from pages.github_home_page import GithubHomePageDesktop, GithubHomePageMobile

@pytest.mark.parametrize(
    "page_class, browser",
    [
        pytest.param(GithubHomePageDesktop, (1920, 1080), marks=pytest.mark.desktop),
        pytest.param(GithubHomePageMobile, (375, 812), marks=pytest.mark.mobile),
    ],
    indirect=["browser"]
)
def test_github_sign_in(page_class, browser):
    page = page_class(browser)
    page.open()
    page.click_sign_in()
    assert "login" in browser.current_url