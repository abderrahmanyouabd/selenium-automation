from behave import given, when, then
from features.pages.login_page import LoginPage

@given('I am on the login page')
def step_impl(context):
    context.driver.get("https://courses.ultimateqa.com/users/sign_in")
    context.login_page = LoginPage(context.driver)

@when('I enter valid credentials')
def step_impl(context):
    context.login_page.login("valid_user@example.com", "valid_password")

@when('I enter invalid credentials')
def step_impl(context):
    context.login_page.login("invalid_user@example.com", "invalid_password")

@then('I should see the dashboard')
def step_impl(context):
    assert context.login_page.is_dashboard_displayed()

@then('I should see an error message')
def step_impl(context):
    assert context.login_page.is_error_message_displayed()