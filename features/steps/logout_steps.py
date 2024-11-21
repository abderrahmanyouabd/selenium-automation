from behave import given, when, then
from pages.menu_page import MenuPage
from selenium.webdriver.common.by import By

@given('I am logged in to SauceDemo as "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.driver.get("https://www.saucedemo.com/")
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.ID, "login-button").click()
    context.menu_page = MenuPage(context.driver)

@when("I click on the menu icon")
def step_impl(context):
    context.menu_page.open_menu()

@when('I click on the "Logout" button')
def step_impl(context):
    context.menu_page.logout()

@then("I should be redirected to the SauceDemo login page")
def step_impl(context):
    assert context.driver.current_url == "https://www.saucedemo.com/"
