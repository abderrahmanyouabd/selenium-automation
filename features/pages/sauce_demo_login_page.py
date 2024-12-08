from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SauceDemoLoginPage:
    LOGIN_URL = "https://www.saucedemo.com/"
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, context):
        self.driver = context.driver

    def open(self):
        self.driver.get(self.LOGIN_URL)

    def login(self, username, password):
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    def wait_for_element(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))

    def click(self, by_locator):
        self.wait_for_element(by_locator)
        self.driver.find_element(*by_locator).click()

    def enter_text(self, by_locator, text):
        self.wait_for_element(by_locator)
        element = self.driver.find_element(*by_locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, by_locator):
        self.wait_for_element(by_locator)
        return self.driver.find_element(*by_locator).text
