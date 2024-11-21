from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SauceDemoLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    
    def wait_for_element(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))

    def click(self, by_locator):
        self.wait_for_element(by_locator)
        self.driver.find_element(*by_locator).click()

    def enter_text(self, by_locator, text):
        self.wait_for_element(by_locator)
        self.driver.find_element(*by_locator).send_keys(text)

    def get_text(self, by_locator):
        self.wait_for_element(by_locator)
        return self.driver.find_element(*by_locator).text
