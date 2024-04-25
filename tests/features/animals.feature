Feature: Manager users and animals
    As a user
    I want to manage my users and animals

    Scenario: Add a user 1
        Given I added a user
        Then the users details are the same on users list and users details

    Scenario: Add a user 2
        Given I am on petclinic
        When I add a user
        Then the users details are displayed on the users list
        And the users details are displayed on the users details

    Scenario: Add a user 3
        Given I a on petclinic homepage
        When I go on find owner page
        And I click on add owner
        And I add a user firstname, lastname, address, city and telephone
        And I click on add owner
        Then the users details are displayed on the users list
        And the users details are displayed on the users details
