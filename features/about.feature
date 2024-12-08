Feature: Demoblaze about us

  Background:
    Given the Demoblaze page is opened

    Scenario: click about us and check if the guidance video is there then close
      Given the "About Us" menu link is clicked
      And the guidance video exists on the page
      Then the "Close Video" button is clicked