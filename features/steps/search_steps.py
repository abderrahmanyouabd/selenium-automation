from behave import given, when, then
from pages.search_page import SearchPage


@given("I am on the GlobalSQA home page")
def step_open_home_page(context):
    context.search_page = SearchPage(context.driver)
    context.search_page.open()
    context.search_page.accept_cookies()


@when('I search for "{term}"')
def step_search_for_term(context, term):
    context.search_page.enter_search_term(term)
    context.search_page.click_search_button()


@then("I should see search results")
def step_verify_search_results(context):
    assert context.search_page.is_results_displayed(), "Search results are not displayed!"


@then('I should see a "No results found" message')
def step_verify_no_results_message(context):
    assert context.search_page.is_no_results_message_displayed(), "No results message is not displayed!"
