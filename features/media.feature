Feature: Verify SauceDemo social media links

  Background:
    Given I am on login page
    And I log in with "standard_user" and password "secret_sauce"

  Scenario Outline: Verify social media links
    Given I am on the SauceDemo footer
    When I click on the "<platform>" icon
    Then Rediraction url should be "<expected_url>"

    Examples:
      | platform  | expected_url                                         |
      | Twitter   | https://x.com/saucelabs                              |
      | Facebook  | https://www.facebook.com/saucelabs                   |
      | LinkedIn  | https://www.linkedin.com/company/sauce-labs/         |