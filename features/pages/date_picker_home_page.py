from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class DatePickerHomePage:
    URL = "https://globalsqa.com/demo-site/datepicker/"
    _cookies_handled = False

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.iframe = (By.CLASS_NAME, "demo-frame")
        self.date_field = (By.XPATH, "//input[@id='datepicker']")
        self.calendar_popup = (By.XPATH, "//table[contains(@class, 'ui-datepicker-calendar')]")
        self.specific_date = "//a[text()='{}']"
        self.cookie_consent_button = (By.XPATH, "//button[contains(@class, 'fc-button') and .='Consent']")

    def open(self):
        """Open the GlobalSQA Date Picker page."""
        self.driver.get(self.URL)

    def handle_cookie_consent(self):
        """Handle cookie consent, ensuring it is done only once."""
        if not DatePickerHomePage._cookies_handled:
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.cookie_consent_button)
                ).click()
                DatePickerHomePage._cookies_handled = True
            except Exception as e:
                print("No cookie consent popup found:", e)

    def switch_to_datepicker_iframe(self):
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(self.iframe)
        )

    def click_date_field(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.date_field)
        ).click()

    def is_calendar_opened(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.calendar_popup)
        )

    def select_date_from_calendar(self, day):
        """Open the calendar and click a specific date."""
        self.click_date_field()
        specific_date_xpath = self.specific_date.format(day)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, specific_date_xpath))
        ).click()

    def get_date_field_value(self):
        """Get the value of the date field in the format MM/DD/YYYY."""
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.date_field)
        ).get_attribute("value")
