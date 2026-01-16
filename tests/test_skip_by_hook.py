import time
import pytest
from pages.github_home_page import GithubHomePageDesktop


@pytest.mark.slow
def test_skip_by_hook(browser):
    time.sleep(6)
    page = GithubHomePageDesktop(browser)
    page.open()
    page.click_sign_in()
    assert "login" in browser.current_url