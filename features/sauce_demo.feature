@SauceDemo
Feature: SauceDemo E2E Testing

  Background:
    Given I am on the SauceDemo login page
    And I log in with username "standard_user" and password "secret_sauce"

  Scenario: Add items to the cart and checkout
    When I add the items "Sauce Labs Backpack" and "Sauce Labs Bolt T-Shirt" to the cart
    Then the cart should contain "2" items
    When I proceed to checkout
    And I fill the checkout information with "John", "Doe", and "12345"
    And I click the finish button
    Then I should see the order confirmation message "Thank you for your order!"