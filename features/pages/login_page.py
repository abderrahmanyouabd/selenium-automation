from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://travelsystem.org/admin/login.php"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Open the login page."""
        self.driver.get(self.URL)

    def enter_email(self, email):
        """Enter email in the email field."""
        email_field = self.driver.find_element(By.ID, "email")
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        """Enter password in the password field."""
        password_field = self.driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(password)

    def submit_login_form(self):
        """Click the submit button to log in."""
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

    def get_error_message(self):
        """Retrieve the error message displayed on the page."""
        try:
            error_element = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.text-group"))
            )
            error_header = error_element.find_element(By.TAG_NAME, "h4").text.strip()
            print(f"Error message header retrieved: {error_header}")
            return error_header
        except TimeoutException:
            print("Error message element not found or not visible.")
            return None
        except NoSuchElementException:
            print("Error message element does not exist on the page.")
            return None
        except Exception as e:
            print(f"Unexpected error occurred while retrieving the error header: {e}")
            return None
