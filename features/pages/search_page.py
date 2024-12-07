from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.cookie_consent_button = (By.XPATH, "//button[contains(@class, 'fc-button') and .='Consent']")
        self.search_input = (By.ID, "s")
        self.search_button = (By.CLASS_NAME, "button_search")
        self.search_results = (By.CSS_SELECTOR, "ol.search_res")
        self.no_results_message = (By.XPATH, "//p[contains(text(), 'Sorry, no posts matched your criteria.')]")


    def accept_cookies(self):
        """
        Accept cookie consent if the popup appears.
        """
        try:
            WebDriverWait(self.driver, 1).until(
                EC.element_to_be_clickable(self.cookie_consent_button)
            ).click()
        except Exception:
            print("No cookie consent popup found.")

    def enter_search_term(self, term):
        """
        Enter a search term in the search input field.
        """
        search_field = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.search_input)
        )
        search_field.clear()
        search_field.send_keys(term)

    def click_search_button(self):
        """
        Click the search button.
        """
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.search_button)
        ).click()

    def is_results_displayed(self):
        """
        Check if search results are displayed.
        """
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.search_results)
            )
            return True
        except Exception:
            return False

    def is_no_results_message_displayed(self):
        """
        Check if the 'no results' message is displayed.
        """
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.no_results_message)
            )
            return True
        except Exception:
            return False
