import pytest
from selenium import webdriver

@pytest.fixture
def browser(request):
    size = request.param if hasattr(request, "param") else (1920, 1080)

    driver = webdriver.Chrome()
    driver.set_window_size(*size)
    driver.implicitly_wait(5)

    yield driver

    driver.quit()
