Feature: Employee users who go onto the homepage should be able to click on the employee login link 

    Scenario: Employee user clicks on the employee login link
        Given I am on the homepage
        When I click on the employee login link
        Then I should be routed to the employee login page