from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SauceDemoCheckoutInformationPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.zip_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")

    def fill_checkout_information(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.zip_code_field).send_keys(zip_code)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()
        print(f"Current URL after clicking Continue: {self.driver.current_url}")