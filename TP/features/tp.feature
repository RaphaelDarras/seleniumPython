Scenario: Selenium Webdriver Python TP
    As a student
    I want to handle Selenium Webdriver Python

    Scenario: Exercise 1
        Given I am logged as "standard_user"
        When I logout
        Then I am back on the login page

    Scenario: Exercise 2
        Given I am on the login page
        When I try to log with the "locked_out_user" credentials
        Then I see an error message

    Scenario: Exercise 3
        Given I am logged as "standard_user"
        When I sort the list in "hilo" order
        And I add the first "2" items in the cart
        And I go to the cart
        And I order as "Raphael" "Darras" habitant au "59000"
        And order informations are correct
        And I finalize the order
        Then the order is confirmed