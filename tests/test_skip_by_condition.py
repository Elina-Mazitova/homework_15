import pytest
from pages.github_home_page import GithubHomePageDesktop, GithubHomePageMobile


@pytest.mark.desktop
@pytest.mark.parametrize(
    "page_class, browser",
    [(GithubHomePageDesktop, (1920, 1080))],
    indirect=["browser"]
)
def test_desktop_skip_by_condition(page_class, browser):
    size = browser.get_window_size()
    if size["width"] < 800:
        pytest.skip("Desktop test skipped on mobile-like resolution")

    page = page_class(browser)
    page.open()
    page.click_sign_in()
    assert "login" in browser.current_url


@pytest.mark.mobile
@pytest.mark.parametrize(
    "page_class, browser",
    [(GithubHomePageMobile, (375, 812))],
    indirect=["browser"]
)
def test_mobile_skip_by_condition(page_class, browser):
    size = browser.get_window_size()
    if size["width"] >= 800:
        pytest.skip("Mobile test skipped on desktop-like resolution")

    page = page_class(browser)
    page.open()
    page.click_sign_in()
    assert "login" in browser.current_url
