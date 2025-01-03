from behave import given, when, then
from pages.menu_page import MenuPage
from selenium.webdriver.common.by import By

@given('I am logged in to SauceDemo as "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.menu_page = MenuPage(context)
    context.menu_page.open()
    context.menu_page.login(username, password)

@when("I click on the menu icon")
def step_impl(context):
    context.menu_page.open_menu()

@when('I click on the "Logout" button')
def step_impl(context):
    context.menu_page.logout()

@then("I should be redirected to the SauceDemo login page")
def step_impl(context):
    expected_url = "https://www.saucedemo.com/"
    assert context.driver.current_url == expected_url, f"Expected URL: {expected_url}, but got {context.driver.current_url}"
