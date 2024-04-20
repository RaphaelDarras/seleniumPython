Feature: Contact form validation
  As a visitor
  I want to ensure that the contact form on the contact page works correctly

  Scenario: Verify the presence of the input field
    Given I am on the contact page
    Then I should see the "nom" input field "text"
    And I should see the "prenom" input field "text"
    And I should see the "email" input field "text"

#  Scenario: Check if input fields and textarea are editable
#    Given I am on the contact page
#    Then I should be able to type in the "nom_user" input field
#    And I should be able to type in the "prenom" input field
#    And I should be able to type in the "email" input field#

#  Scenario: Submit mon form
#    Given I am on the contact page
#    Then I click on submit button to send "formulaire"
#    Then I should see the confirmation message##

#  Scenario: Verify labels for each input
#    Given I am on the contact page
#    Then I should see a label for the "nom" input field
#    And I should see a label for the "prenom" input field
#    And I should see a label for the "email" input field
#    And I should see a label for the "message" textarea
