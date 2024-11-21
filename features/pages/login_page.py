from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.ID, "user_email")
        self.password_field = (By.ID, "user_password")
        self.login_button = (By.NAME, "commit")
        self.error_message = (By.CSS_SELECTOR, ".alert-danger")

    def login(self, email, password):
        self.driver.find_element(*self.email_field).send_keys(email)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def is_dashboard_displayed(self):
        # Implement logic to verify dashboard display
        pass

    def is_error_message_displayed(self):
        return self.driver.find_element(*self.error_message).is_displayed()
