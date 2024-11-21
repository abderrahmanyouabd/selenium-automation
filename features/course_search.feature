Feature: Course search functionality

  Scenario: Search for an existing course
    Given I am on the homepage
    When I search for an existing course
    Then I should see the course details

  Scenario: Search for a non-existent course
    Given I am on the homepage
    When I search for a non-existent course
    Then I should see a no results message
