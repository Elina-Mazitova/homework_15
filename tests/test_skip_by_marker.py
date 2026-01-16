import pytest
from pages.github_home_page import GithubHomePageDesktop


@pytest.mark.skip(reason="Этот тест пропущен через маркер skip")
def test_skip_by_marker(browser):
    page = GithubHomePageDesktop(browser)
    page.open()
    page.click_sign_in()
    assert "login" in browser.current_url
