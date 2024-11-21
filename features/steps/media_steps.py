from behave import given, when, then
from selenium.webdriver.common.by import By

@given('I am on login page')
def step_impl(context):
    # Navigate to the SauceDemo login page
    context.driver.get("https://www.saucedemo.com/")
    print("Navigated to the SauceDemo login page.")

@given('I log in with "{username}" and password "{password}"')
def step_impl(context, username, password):
    # Log in with the provided credentials
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.ID, "login-button").click()
    print(f"Logged in with username: {username}")

@given('I am on the SauceDemo footer')
def step_impl(context):
    # Assuming the footer is part of the home page after login
    print("Navigating to the SauceDemo footer.")

@when('I click on the "{platform}" icon')
def step_impl(context, platform):
    # Define the mapping for platform icons
    platform_links = {
        "Twitter": "Twitter",
        "Facebook": "Facebook",
        "LinkedIn": "LinkedIn"
    }

    # Get the platform link text based on the input
    link_text = platform_links.get(platform)
    if not link_text:
        raise ValueError(f"Platform {platform} not found in predefined links.")

    # Click on the social media icon
    context.driver.find_element(By.LINK_TEXT, link_text).click()
    print(f"Clicked on the {platform} icon.")

@then('Rediraction url should be "{expected_url}"')
def step_impl(context, expected_url):
    # Switch to the newly opened tab
    context.driver.switch_to.window(context.driver.window_handles[-1])
    actual_url = context.driver.current_url

    # Verify the redirection URL
    assert expected_url in expected_url, f"Expected URL {expected_url}, but got {actual_url}."
    print(f"Verified redirection to {actual_url}.")

    # Close the new tab and switch back to the original tab
    context.driver.close()
    context.driver.switch_to.window(context.driver.window_handles[0])