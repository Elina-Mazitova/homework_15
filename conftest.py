import time
import pytest
import allure
from selenium import webdriver


SLOW_THRESHOLD = 5.0

def pytest_runtest_setup(item):
    item.start_time = time.time()
    print(f"\n=== START TEST: {item.name} ===")


def pytest_collection_modifyitems(config, items):
    for item in items:

        if "mobile" in item.keywords:
            item.user_properties.append(("device", "mobile"))

        if "desktop" in item.keywords:
            item.user_properties.append(("device", "desktop"))

        if "slow" in item.keywords:
            item.add_marker(pytest.mark.skip(reason="Skipping slow tests (duration > 5s)"))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)

    if rep.when == "call":
        duration = time.time() - item.start_time
        item.duration = duration
        print(f"=== TEST DURATION: {duration:.2f} seconds ===")

        if duration > SLOW_THRESHOLD:
            item.add_marker(pytest.mark.slow)
            print(f"=== TEST MARKED AS SLOW (duration {duration:.2f}s) ===")

@pytest.fixture
def browser(request):
    size = request.param if hasattr(request, "param") else (1920, 1080)

    driver = webdriver.Chrome()
    driver.set_window_size(*size)
    driver.implicitly_wait(5)

    yield driver

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:

        with allure.step("Скриншот при падении"):
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("HTML страницы при падении"):
            allure.attach(
                driver.page_source,
                name="page_source",
                attachment_type=allure.attachment_type.HTML
            )

    driver.quit()
