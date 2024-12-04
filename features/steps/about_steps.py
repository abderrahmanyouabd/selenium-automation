from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@given('the "About Us" menu link is clicked')
def step_impl(context):
    # Click the "About Us" menu link
    about_us_link = context.driver.find_element(By.LINK_TEXT, "About us")
    about_us_link.click()

@given('the guidance video is existed')
def step_impl(context):
    try:
        # Wait for the guidance video to appear
        WebDriverWait(context.driver, 5).until(
            EC.presence_of_element_located((By.ID, "example-video"))
        )
        print("Guidance video is displayed.")
    except TimeoutException:
        assert False, "Guidance video is not displayed."

@then('the "Close Video" button is clicked')
def step_impl(context):
    try:
        # Wait for the "Close Video" button to be clickable
        close_button = WebDriverWait(context.driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#videoModal .modal-footer .btn"))
        )
        close_button.click()
    except TimeoutException:
        assert False, '"Close Video" button is not clickable.'
