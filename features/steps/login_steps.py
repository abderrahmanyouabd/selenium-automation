from behave import given, when, then
from features.pages.login_page import LoginPage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the demo login page')
def step_impl(context):
    context.driver.get("https://travelsystem.org/admin/login.php")
    context.login_page = LoginPage(context.driver)

@when('I fill the "{field}" field with "{value}"')
def step_impl(context, field, value):
    if field.lower() == 'email':
        if value == '[BLANK]':
            value = ""
        context.login_page.enter_email(value)
    elif field.lower() == 'password':
        if value == '[BLANK]':
            value = ""
        context.login_page.enter_password(value)

@when('I submit the login form')
def step_impl(context):
    context.login_page.submit_login_form()

@then('I should be redirected to "{expected_url}"')
def step_impl(context, expected_url):
    try:
        if expected_url != "[BLANK]":
            WebDriverWait(context.driver, 10).until(EC.url_contains(expected_url))
            current_url = context.driver.current_url
            assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"
            print(f"Successfully redirected to: {current_url}")
        else:
            print("No redirection expected.")
    except TimeoutException:
        print(f"Timed out waiting for redirection to {expected_url}")
        raise
    except Exception as e:
        print(f"Error during redirection verification: {e}")
        raise



@then('I should see the login message "{expected_message}"')
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

        if actual_message is None:
            actual_message = context.login_page.get_error_message()


        if expected_message != "N/A":
            assert actual_message is not None, "No error or alert message was detected."
            assert expected_message == actual_message, f"Expected '{expected_message}', but got '{actual_message}'"
            print(f"Login message verified: {actual_message}")
        else:
            print("No error message expected for this scenario.")
    except Exception as e:
        print(f"Error verifying the login message: {e}")
        raise
