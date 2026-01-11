from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GithubHomePageDesktop:
    SIGN_IN_BUTTON = (By.LINK_TEXT, "Sign in")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://github.com")

    def click_sign_in(self):
        self.driver.find_element(*self.SIGN_IN_BUTTON).click()


class GithubHomePageMobile:
    MENU_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Toggle navigation"], summary[aria-label="Toggle navigation"]')
    SIGN_IN_LINK = (By.LINK_TEXT, "Sign in")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://github.com")

    def click_sign_in(self):
        menu = self.wait.until(EC.presence_of_element_located(self.MENU_BUTTON))
        self.driver.execute_script("arguments[0].click();", menu)

        sign_in = self.wait.until(EC.presence_of_element_located(self.SIGN_IN_LINK))
        self.driver.execute_script("arguments[0].click();", sign_in)