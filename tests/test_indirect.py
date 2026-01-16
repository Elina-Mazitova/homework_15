import pytest
from pages.github_home_page import GithubHomePageDesktop


@pytest.mark.parametrize(
    "browser",
    [(1920, 1080), (375, 812)],
    indirect=True
)
def test_indirect(browser):
    page = GithubHomePageDesktop(browser)
    page.open()
    page.click_sign_in()
    assert "login" in browser.current_url
