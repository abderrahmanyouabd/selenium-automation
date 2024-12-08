from behave import given, when, then
from pages.date_picker_home_page import DatePickerHomePage


@given("I am on the GlobalSQA Date Picker page")
def step_open_date_picker_page(context):
    context.date_picker_page = DatePickerHomePage(context.driver)
    context.date_picker_page.open()
    context.date_picker_page.handle_cookie_consent()
    context.date_picker_page.switch_to_datepicker_iframe()


@when('I click on the "Date" field')
def step_click_date_field(context):
    context.date_picker_page.click_date_field()


@then("the Date Picker calendar should open")
def step_verify_calendar_open(context):
    assert context.date_picker_page.is_calendar_opened(), "Calendar did not open!"


@when('I select the date "{date_to_select}"')
def step_select_date(context, date_to_select):
    day = date_to_select.split("-")[2]
    context.date_picker_page.select_date_from_calendar(day)


@then('the "Date" field should display "{expected_date}"')
def step_verify_date_field(context, expected_date):
    actual_date = context.date_picker_page.get_date_field_value()
    assert actual_date == expected_date, f"Expected date: {expected_date}, but got: {actual_date}"


@then("quit the browser")
def step_quit_browser(context):
    context.driver.quit()
