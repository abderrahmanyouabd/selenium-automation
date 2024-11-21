from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "search-courses")
        self.search_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.course_title = (By.CSS_SELECTOR, ".course-title")
        self.no_results_message = (By.CSS_SELECTOR, ".no-results-message")

    def search_course(self, course_name):
        self.driver.find_element(*self.search_box).send_keys(course_name)
        self.driver.find_element(*self.search_button).click()

    def is_course_displayed(self, course_name):
        courses = self.driver.find_elements(*self.course_title)
        return any(course_name in course.text for course in courses)

    def is_no_results_message_displayed(self):
        return self.driver.find_element(*self.no_results_message).is_displayed()