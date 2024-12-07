from behave import given, when, then
from selenium.webdriver.common.by import By

@given('I am on login page')
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/")
    print("Navigated to the SauceDemo login page.")

@given('I log in with "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.ID, "login-button").click()
    print(f"Logged in with username: {username}")

@given('I am on the SauceDemo footer')
def step_impl(context):
    print("Navigating to the SauceDemo footer.")

@when('I click on the "{platform}" icon')
def step_impl(context, platform):
    platform_links = {
        "Twitter": "Twitter",
        "Facebook": "Facebook",
        "LinkedIn": "LinkedIn"
    }

    link_text = platform_links.get(platform)
    if not link_text:
        raise ValueError(f"Platform {platform} not found in predefined links.")

    context.driver.find_element(By.LINK_TEXT, link_text).click()
    print(f"Clicked on the {platform} icon.")

@then('Rediraction url should be "{expected_url}"')
def step_impl(context, expected_url):
    context.driver.switch_to.window(context.driver.window_handles[-1])
    actual_url = context.driver.current_url
    assert expected_url in expected_url, f"Expected URL {expected_url}, but got {actual_url}."
    print(f"Verified redirection to {actual_url}.")

    context.driver.close()
    context.driver.switch_to.window(context.driver.window_handles[0])