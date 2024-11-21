from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

class DemoRegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators (using XPATH)
        self.locators = {
            "first_name_field": (By.XPATH, "//input[@name='first_name']"),
            "last_name_field": (By.XPATH, "//input[@name='last_name']"),
            "email_field": (By.XPATH, "//input[@name='email']"),
            "whatsapp_field": (By.XPATH, "//input[@name='whatsapp']"),
            "country_dropdown": (By.XPATH, "//select[@id='country_id']"),
            "business_name_field": (By.XPATH, "//input[@name='business_name']"),
            "result_field": (By.XPATH, "//input[@id='number']"),
            "submit_button": (By.XPATH, "//button[@id='demo']"),
            "error_message": (By.XPATH, "//div[contains(@class, 'alert_msg')]"),
            "num1": (By.ID, "numb1"),
            "num2": (By.ID, "numb2"),
        }

    def handle_alert(self):
        try:
            alert = self.driver.switch_to.alert
            print(f"Alert detected: {alert.text}")
            alert.accept()
        except Exception as e:
            print(f"No alert present to handle: {e}")

    def fill_first_name(self, first_name):
        self._fill_field(self.locators["first_name_field"], first_name, "First Name")

    def fill_last_name(self, last_name):
        self._fill_field(self.locators["last_name_field"], last_name, "Last Name")

    def fill_email(self, email):
        self._fill_field(self.locators["email_field"], email, "Email")

    def fill_whatsapp(self, whatsapp):
        self._fill_field(self.locators["whatsapp_field"], whatsapp, "WhatsApp")

    def select_country(self, country_id):
        self._select_dropdown(self.locators["country_dropdown"], country_id, "Country Dropdown")

    def fill_business_name(self, business_name):
        self._fill_field(self.locators["business_name_field"], business_name, "Business Name")

    def _fill_field(self, locator, value, field_name):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.clear()
            element.send_keys(value)
            print(f"{field_name} filled with: {value}")
        except UnexpectedAlertPresentException:
            print(f"Unexpected alert appeared while filling {field_name}!")
            self.handle_alert()
        except Exception as e:
            print(f"Error while filling {field_name}: {e}")

    def _select_dropdown(self, locator, value, dropdown_name):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            select = Select(element)
            select.select_by_value(value)
            print(f"{dropdown_name} selected: {value}")
        except UnexpectedAlertPresentException:
            print(f"Unexpected alert appeared while selecting {dropdown_name}!")
            self.handle_alert()
        except Exception as e:
            print(f"Error while selecting {dropdown_name}: {e}")

    def submit_form(self):
        try:
            # Calculate and fill the result field before submission
            num1 = int(self.wait.until(EC.visibility_of_element_located(self.locators["num1"])).text)
            num2 = int(self.wait.until(EC.visibility_of_element_located(self.locators["num2"])).text)
            result = num1 + num2
            print(f"Ensuring result is set before submitting: {num1} + {num2} = {result}")

            # Fill the result field
            result_field = self.wait.until(EC.element_to_be_clickable(self.locators["result_field"]))
            result_field.clear()  # Clear any existing value
            result_field.send_keys(str(result))
            print("Result field filled successfully before submission.")

            # Click the submit button
            self.wait.until(EC.element_to_be_clickable(self.locators["submit_button"])).click()
            print("Form submitted successfully.")
        except UnexpectedAlertPresentException as e:
            print(f"Unexpected alert encountered: {e}")
            self.handle_alert()  # Handle the alert to proceed
        except Exception as e:
            print(f"Error before or during form submission: {e}")

    def get_error_message(self):
        try:
            # Locate the error message using CSS selector
            error_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert_msg p")))
            error_message = error_element.text.strip()
            print(f"Error message retrieved: {error_message}")
            return error_message
        except TimeoutException:
            print("Error message element not found or not visible.")
            return None
        except NoSuchElementException:
            print("Error message element does not exist on the page.")
            return None
        except Exception as e:
            print(f"Unexpected error occurred while retrieving the error message: {e}")
            return None

