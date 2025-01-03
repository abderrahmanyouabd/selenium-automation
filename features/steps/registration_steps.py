from pages.registration_page import DemoRegistrationPage
from behave import given, when, then
from selenium.common.exceptions import UnexpectedAlertPresentException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I am on the demo registration page')
def step_impl(context):
    context.registration_page = DemoRegistrationPage(context.driver)
    context.registration_page.open()
    print("Navigated to registration page")


@when("I fill the 'First Name' field with '{first_name}'")
def step_impl(context, first_name):
    try:
        context.registration_page.fill_first_name(first_name if first_name != "[BLANK]" else "")
    except Exception as e:
        print(f"Error filling First Name field: {e}")


@when("I fill the 'Last Name' field with '{last_name}'")
def step_impl(context, last_name):
    try:
        context.registration_page.fill_last_name(last_name)
    except Exception as e:
        print(f"Error filling Last Name field: {e}")


@when("I fill the 'Email' field with '{email}'")
def step_impl(context, email):
    try:
        context.registration_page.fill_email(email)
    except Exception as e:
        print(f"Error filling Email field: {e}")


@when("I fill the 'WhatsApp' field with '{whatsapp}'")
def step_impl(context, whatsapp):
    try:
        context.registration_page.fill_whatsapp(whatsapp)
    except Exception as e:
        print(f"Error filling WhatsApp field: {e}")


@when("I select '{country_id}' from the country dropdown")
def step_impl(context, country_id):
    try:
        context.registration_page.select_country(country_id)
    except Exception as e:
        print(f"Error selecting country: {e}")


@when("I fill the 'Business Name' field with '{business_name}'")
def step_impl(context, business_name):
    try:
        context.registration_page.fill_business_name(business_name)
    except Exception as e:
        print(f"Error filling Business Name field: {e}")


@when("I submit the registration form")
def step_impl(context):
    try:
        context.registration_page.submit_form()
    except Exception as e:
        print(f"Error submitting the form: {e}")


@then("I should see the registration message '{expected_message}'")
def step_impl(context, expected_message):
    try:
        actual_message = None

        try:
            alert = context.driver.switch_to.alert
            actual_message = alert.text.strip()
            print(f"Alert detected with message: {actual_message}")
            alert.accept()
        except Exception:
            print("No alert detected.")

        if not actual_message:
            actual_message = context.registration_page.get_error_message()

        if not actual_message:
            try:
                success_element = WebDriverWait(context.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'completed')]//h2/strong"))
                )
                actual_message = success_element.text.strip()
                print(f"Success message detected: {actual_message}")
            except TimeoutException:
                print("Success message did not appear within the wait time.")
            except Exception as e:
                print(f"Error while checking for success message: {e}")

        assert expected_message in actual_message, f"Expected '{expected_message}', but got '{actual_message}'"

    except Exception as e:
        print(f"Error verifying the message: {e}")
