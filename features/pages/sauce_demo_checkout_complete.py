from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class SauceDemoCheckoutCompletePage:
    def __init__(self, driver):
        self.driver = driver
        self.finish_button = (By.ID, "finish")
        self.order_confirmation_message = (By.CLASS_NAME, 'complete-header')

    def click_finish(self):
        self.driver.find_element(*self.finish_button).click()
        print("Finish button clicked.")

    def get_order_confirmation_message(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.order_confirmation_message)
        )
        return self.driver.find_element(*self.order_confirmation_message).text
