@Login
Feature: Login functionality

  Background:
    Given I am on the demo login page

  Scenario Outline: Login scenarios
    When I fill the "Email" field with "<email>"
    And I fill the "Password" field with "<password>"
    And I submit the login form
    Then I should see the login message "<expected_message>"
    And I should be redirected to "<expected_url>"

    Examples:
      | email                  | password   | expected_url                               | expected_message                |
      | agent@phptravels.com   | demoadmin  | https://phptravels.net/admin/login.php     | Invalid Login                   |
      | [BLANK]                | demoadmin  | https://phptravels.net/admin/login.php     | Email is required to login      |
      | admin@phptravels.com   | agentadmin | https://phptravels.net/admin/login.php     | Invalid Login                   |
      | admin@phptravels.com   | demoadmin  | https://phptravels.net/admin/dashboard.php | N/A                             |