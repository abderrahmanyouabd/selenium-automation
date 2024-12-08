from behave import given, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@given('the "Contact Link" menu link is clicked')
def step_click_contact_link(context):
    """Click the 'Contact' link in the menu."""
    contact_link = context.driver.find_element(By.LINK_TEXT, "Contact")
    contact_link.click()


@given('the contact "{field}" field is filled with "{value}"')
def step_fill_contact_field(context, field, value):
    """Fill in a field in the 'Contact Us' form."""
    field_ids = {
        "Contact Email:": "recipient-email",
        "Contact Name:": "recipient-name",
        "Message:": "message-text"
    }
    field_id = field_ids.get(field)
    if not field_id:
        raise ValueError(f"Field '{field}' is not recognized.")
    
    field_element = WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located((By.ID, field_id))
    )
    field_element.clear()
    field_element.send_keys(value)


@given('the "Send Message" button is clicked')
def step_click_send_message(context):
    """Click the 'Send Message' button and handle the alert."""
    send_button = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#exampleModal .modal-footer .btn-primary"))
    )
    send_button.click()
    try:
        WebDriverWait(context.driver, 5).until(EC.alert_is_present())
        alert = context.driver.switch_to.alert
        alert.accept()
    except TimeoutException:
        assert False, 'No alert appeared after clicking "Send Message".'


@then('the "Contact Us" popup should be closed')
def step_verify_popup_closed(context):
    """Verify that the 'Contact Us' popup is closed."""
    try:
        WebDriverWait(context.driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal-content"))
        )
    except TimeoutException:
        assert False, 'The "Contact Us" popup was not closed as expected.'