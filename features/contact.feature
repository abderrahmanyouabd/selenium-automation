Feature: Demoblaze contact

  Background:
    Given the Demoblaze home page is opened

    Scenario: Send a contact us message
      Given the "Contact Link" menu link is clicked
      And the contact "Contact Email:" field is filled with "roomacc250@gmail.com"
      And the contact "Contact Name:" field is filled with "a1st"
      And the contact "Message:" field is filled with "I'm just testing, ignore me :)"
      And the "Send Message" button is clicked
      Then the "Contact Us" popup should be closed