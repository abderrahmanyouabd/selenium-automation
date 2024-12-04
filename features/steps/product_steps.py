from behave import given, when, then
from selenium import webdriver
from pages.demo_blaze_home_page import HomePage, CartPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@given('the Demoblaze home page is opened')
def step_impl(context):
    context.driver.get("https://www.demoblaze.com/index.html")
    context.home_page = HomePage(context.driver)
    context.cart_page = CartPage(context.driver)

@given('the "{item}" item is clicked')
def step_impl(context, item):
    context.home_page.click_item(item)

@given('the "Add to cart" button is clicked')
def step_impl(context):
    context.cart_page.click_button("Add to cart")
    try:
        # Handle the alert
        WebDriverWait(context.driver, 5).until(EC.alert_is_present())
        alert = context.driver.switch_to.alert
        alert.accept()
    except TimeoutException:
        print("No alert appeared after clicking 'Add to cart'.")

@given('the "Home" button is clicked')
def step_impl(context):
    context.home_page.click_button("Home")

@given('the "Cart" button is clicked')
def step_impl(context):
    context.home_page.click_button("Cart")

@when('the "Delete {item}" button is clicked')
def step_impl(context, item):
    context.cart_page.delete_item(item)

@then('the total price should read "{expected_price}"')
def step_impl(context, expected_price):
    total_price = context.cart_page.get_total_price()
    assert total_price == int(expected_price), f"Expected {expected_price}, but got {total_price}"

@when('the "Place Order" button is clicked')
def step_impl(context):
    context.cart_page.click_button("Place Order")

@when('the "{field}" field is filled with "{value}"')
def step_impl(context, field, value):
    fields = {
        "Name:": "name",
        "Country:": "country",
        "City:": "city",
        "Credit card:": "card",
        "Month:": "month",
        "Year:": "year",
    }
    context.driver.find_element(By.ID, fields[field]).send_keys(value)

@when('the "Purchase" button is clicked')
def step_impl(context):
    context.cart_page.click_button("Purchase")
