from behave import given, when, then
from selenium.webdriver.common.by import By
from pages.sauce_demo_login_page import SauceDemoLoginPage
from pages.sauce_demo_cart_page import SauceDemoCartPage
from pages.sauce_demo_checkout_page import SauceDemoCheckoutInformationPage
from pages.sauce_demo_checkout_complete import SauceDemoCheckoutCompletePage
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@given('I am on the SauceDemo login page')
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/")
    context.login_page = SauceDemoLoginPage(context.driver)

@given('I log in with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)
    try:
        while True:  # Keep checking and accepting alerts
            alert = context.driver.switch_to.alert
            print(f"Alert detected: {alert.text}")  # Optional, for debugging
            alert.accept()
            print("Alert accepted.")
    except NoAlertPresentException:
        print("No more alerts present.")

@when('I add the items "{item1}" and "{item2}" to the cart')
def step_impl(context, item1, item2):
    try:
        # Click the "Add to Cart" button for item1
        context.driver.find_element(By.XPATH, f"//div[text()='{item1}']/ancestor::div[@class='inventory_item']//button").click()
        print(f"Added {item1} to the cart.")

        # Click the "Add to Cart" button for item2
        context.driver.find_element(By.XPATH, f"//div[text()='{item2}']/ancestor::div[@class='inventory_item']//button").click()
        print(f"Added {item2} to the cart.")
    except Exception as e:
        print(f"Error while adding items to the cart: {e}")
        raise


@then('the cart should contain "{count}" items')
def step_impl(context, count):
    cart_page = SauceDemoCartPage(context.driver)
    cart_item_count = cart_page.get_cart_item_count()
    print(f"Cart contains {cart_item_count} items.")  # Debugging info
    assert cart_item_count == int(count), f"Expected {count} items, but found {cart_item_count}."

@when('I proceed to checkout')
def step_impl(context):
    cart_page = SauceDemoCartPage(context.driver)
    cart_page.open_cart()
    cart_page.click_checkout()
    print("Proceeded to checkout.")


@when('I fill the checkout information with "{first_name}", "{last_name}", and "{zip_code}"')
def step_impl(context, first_name, last_name, zip_code):
    # Use the checkout information page
    context.checkout_information_page = SauceDemoCheckoutInformationPage(context.driver)
    context.checkout_information_page.fill_checkout_information(first_name, last_name, zip_code)
    context.checkout_information_page.click_continue()

@when('I click the finish button')
def step_impl(context):
    context.checkout_page = SauceDemoCheckoutCompletePage(context.driver)
    context.checkout_page.click_finish()

@then('I should see the order confirmation message "{message}"')
def step_impl(context, message):
    context.checkout_page = SauceDemoCheckoutCompletePage(context.driver)
    confirmation_message = context.checkout_page.get_order_confirmation_message()
    assert confirmation_message == message, f"Expected confirmation message '{message}', but got '{confirmation_message}'"
    print(f"Order confirmation message verified: {confirmation_message}")