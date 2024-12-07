@DatePicker
Feature: Test Date Picker functionality on GlobalSQA

  Background:
    Given I am on the GlobalSQA Date Picker page

  Scenario: Select a valid date
    When I click on the "Date" field
    And I select the date "2024-12-29"
    Then the "Date" field should display "12/29/2024"

  Scenario: Select another valid date
    When I click on the "Date" field
    And I select the date "2024-12-11"
    Then the "Date" field should display "12/11/2024"