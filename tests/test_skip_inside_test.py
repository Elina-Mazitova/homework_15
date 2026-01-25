import pytest
from pages.github_home_page import GithubHomePageDesktop, GithubHomePageMobile


@pytest.mark.parametrize(
    "page_class, size",
    [
        (GithubHomePageDesktop, (1920, 1080)),
        (GithubHomePageMobile, (375, 812)),
    ]
)
def test_skip_inside_test(page_class, size, browser):
    browser.set_window_size(*size)

    if size[0] < 800:
        pytest.skip("Пропускаем мобильные разрешения")

    page = page_class(browser)
    page.open()
    page.click_sign_in()

    assert "login" in browser.current_url