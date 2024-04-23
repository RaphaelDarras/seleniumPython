Feature: Contact form validation
    As a visitor
    I want to ensure that the contact page works correctly

    Scenario: Verify the presence of the input field
        Given I am on the contact page
        Then I should see the "nom" input field "text"

    Scenario: Verify input field is disabled
        Given I am on the contact page
        Then I should see the "nom" is disabled
        And I should see the "prenom" is enabled

    Scenario: Verify label text
        Given I am on the contact page
        Then I should see the "nom" label is equal to "Votre Nom" 

    Scenario: Write in a field
        Given I am on the contact page
        Then I can write "toto" in the field "message"

    Scenario: I can change page
        Given I am on the index page
        When I click on the contact link
        Then I am redirected on the contact page

    Scenario: Compare values on two pages
        Given I am on the index page with a value to compare
        When I click on the contact link
        Then I am redirected on the contact page
        And the values to compare are equals

    Scenario: I can select a fruit
        Given I am on the index page
        Then I can select mango in the fruits dropdown
