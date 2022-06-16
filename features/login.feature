Feature: Users who go on the login page should be able to log into their account

    Scenario Outline: Employee user logs into their account with valid inputs
        Given I am on employee login page
        When I input a valid username <username>
        When I input a valid password <password>
        When I click on the Submit button
        Then I should be on the page with title Employee account page

        Examples:
            | username | password |
            | billy    | pass1234 |

    Scenario Outline: Manager user logs into their account with valid inputs
        Given I am on manager login page
        When I input a valid username <username>
        When I input a valid password <password>
        When I click on the Submit button
        Then I should be on the page with title Manager account page

        Examples:
            | username | password |
            | smith    | pass1234 |
