@SauceDemo
Feature: SauceDemo Testing

  Background:
    Given I am on the SauceDemo login page
    And I log in with username "standard_user" and password "secret_sauce"

  Scenario Outline: Add items to the cart and checkout
    When I add the items "<items>" to the cart
    Then the cart should contain "<cart_count>" items
    When I proceed to checkout
    And I fill the checkout information with "<first_name>", "<last_name>", and "<postal_code>"
    And I click the finish button
    Then I should see the order confirmation message "<confirmation_message>"

    Examples:
      | items                                      | cart_count | first_name | last_name | postal_code | confirmation_message              |
      | Sauce Labs Backpack, Sauce Labs Onesie     | 2          | John       | Doe       | 12345       | Thank you for your order!         |
      | Sauce Labs Bike Light                      | 1          | Jane       | Smith     | 54321       | Thank you for your order!         |
      | Sauce Labs Fleece Jacket                   | 1          | Alice      | Brown     | 67890       | Thank you for your order!         |
      | Sauce Labs Bolt T-Shirt, Sauce Labs Onesie | 2          | Bob        | White     | 11111       | Thank you for your order!         |
      | Sauce Labs Backpack, Sauce Labs Onesie     | 2          | Emily      | Davis     | 22222       | Thank you for your order!         |
      | Sauce Labs Bike Light, Sauce Labs Onesie   | 2          | Chris      | Green     | 33333       | Thank you for your order!         |