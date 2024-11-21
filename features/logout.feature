Feature: Logout functionality

  Scenario: Logout from the application
    Given I am logged in to SauceDemo as "standard_user" with password "secret_sauce"
    When I click on the menu icon
    And I click on the "Logout" button
    Then I should be redirected to the SauceDemo login page
