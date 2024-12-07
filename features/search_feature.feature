@SearchFeature
Feature: Search functionality on GlobalSQA

  Background:
    Given I am on the GlobalSQA home page

  Scenario: Perform a valid search
    When I search for "android"
    Then I should see search results

  Scenario: Perform an invalid search
    When I search for "crazy"
    Then I should see a "No results found" message
