@Registration
Feature: Registration functionality

  Background:
    Given I am on the demo registration page

  Scenario Outline: Registration scenarios
    When I fill the 'First Name' field with '<first_name>'
    And I fill the 'Last Name' field with '<last_name>'
    And I fill the 'Email' field with '<email>'
    And I fill the 'WhatsApp' field with '<whatsapp>'
    And I select '<country_id>' from the country dropdown
    And I fill the 'Business Name' field with '<business_name>'
    And I submit the registration form
    Then I should see the registration message '<expected_message>'

    Examples:
      | first_name | last_name | email                | whatsapp   | country_id  | business_name  | expected_message         |
      | John       | Doe       | roomacc250@gmail.com | 305662128  | 97          | MyBusiness     | Thank you!   |
      | John       | Doe       | invalid-email        | 1234567890 | 97          | MyBusiness     | Email address is not valid. please use real email address    |
      | John       | Doe       | roomacc250@gmail.com | [BLANK]    | 97          | MyBusiness     | Please type your whatsapp number    |
      | [BLANK]    | Doe       | roomacc250@gmail.com | 1234567890 | 97          | MyBusiness     | Please type your first name   |
