from behave import given, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

@given('the "Contact Link" menu link is clicked')
def step_impl(context):
    # Click the "Contact Link" menu link
    contact_link = context.driver.find_element(By.LINK_TEXT, "Contact")
    contact_link.click()

@given('the contact "Contact Email:" field is filled with "{email}"')
def step_impl(context, email):
    # Fill the "Contact Email" field
    email_field = WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located((By.ID, "recipient-email"))
    )
    email_field.clear()
    email_field.send_keys(email)

@given('the contact "Contact Name:" field is filled with "{name}"')
def step_impl(context, name):
    # Fill the "Contact Name" field
    name_field = WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located((By.ID, "recipient-name"))
    )
    name_field.clear()
    name_field.send_keys(name)

@given('the contact "Message:" field is filled with "{message}"')
def step_impl(context, message):
    # Fill the "Message" field
    message_field = WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located((By.ID, "message-text"))
    )
    message_field.clear()
    message_field.send_keys(message)

@given('the "Send Message" button is clicked')
def step_impl(context):
    # Click the "Send Message" button
    send_button = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#exampleModal .modal-footer .btn-primary"))
    )
    send_button.click()
    try:
        # Handle the alert
        WebDriverWait(context.driver, 5).until(EC.alert_is_present())
        alert = context.driver.switch_to.alert
        alert.accept()
    except TimeoutException:
        print('No alert appeared after clicking "Send Message".')

@then('the "Contact Us" popup should be closed')
def step_impl(context):
    try:
        # Wait for the modal popup to become invisible
        WebDriverWait(context.driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal-content"))
        )
        print('The "Contact Us" popup was successfully closed.')
    except TimeoutException:
        # Raise an assertion failure if the modal does not disappear
        assert False, 'The "Contact Us" popup was not closed as expected.'


