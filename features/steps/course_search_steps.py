from behave import given, when, then
from features.pages.home_page import HomePage

@given('I am on the homepage')
def step_impl(context):
    context.driver.get("https://courses.ultimateqa.com/")
    context.home_page = HomePage(context.driver)

@when('I search for an existing course')
def step_impl(context):
    context.home_page.search_course("Selenium WebDriver with Java")

@when('I search for a non-existent course')
def step_impl(context):
    context.home_page.search_course("NonExistent Course")

@then('I should see the course details')
def step_impl(context):
    assert context.home_page.is_course_displayed("Selenium WebDriver with Java")

@then('I should see a no results message')
def step_impl(context):
    assert context.home_page.is_no_results_message_displayed()
