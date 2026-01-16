import time
import pytest
from pages.github_home_page import GithubHomePageDesktop, GithubHomePageMobile


@pytest.mark.desktop
@pytest.mark.parametrize(
    "page_class, browser",
    [
        pytest.param(GithubHomePageDesktop, (1920, 1080), marks=pytest.mark.desktop),
    ],
    indirect=["browser"]
)
def test_github_sign_in_desktop(page_class, browser):
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
    [
        pytest.param(GithubHomePageMobile, (375, 812), marks=pytest.mark.mobile),
    ],
    indirect=["browser"]
)
def test_github_sign_in_mobile(page_class, browser):
    size = browser.get_window_size()
    if size["width"] >= 800:
        pytest.skip("Mobile test skipped on desktop-like resolution")

    time.sleep(5)

    page = page_class(browser)
    page.open()
    page.click_sign_in()
    assert "login" in browser.current_url
