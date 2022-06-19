Feature: Users who logon should be able to make view previous requests, and cancel

    Scenario Outline: User should be able to view previous requests
        Given emp user2 on login page
        When emp user2 inputs username <username>
        When emp user2 inputs password <password>
        When emp user2 clicks submit on login page
        Then emp user2 is on account page
        When emp user2 clicks on view previous requests
        Then emp user2 is on view previous request page

        Examples:
            | username | password |
            | billy    | pass1234 |

    Scenario Outline: User should be able to cancel requests
        Given emp user2 on login page
        When emp user2 inputs username <username>
        When emp user2 inputs password <password>
        When emp user2 clicks submit on login page
        Then emp user2 is on account page
        When emp user2 clicks on view previous requests
        Then emp user2 is on view previous request page
        When emp user2 clicks on cancel request
        Then emp user2 should be on view request page with request status updated to cancelled

        Examples:
            | username | password |
            | billy    | pass1234 |

    Scenario Outline: Manager should be able to view previous requests
        Given I am on manager login page
        When I input a valid username <username>
        When I input a valid password <password>
        When I click on the Submit button
        Then I should be on the page with title Manager account page
        When I click on manager view previous requests
        Then I am on manager view previous request page

        Examples:
            | username | password |
            | smith    | pass1234 |

    Scenario Outline: Manager should be able to cancel requests
        Given I am on manager login page
        When I input a valid username <username>
        When I input a valid password <password>
        When I click on the Submit button
        Then I should be on the page with title Manager account page
        When I click on manager view previous requests
        Then I am on manager view previous request page
        When I click on cancel request
        Then I should be on view request page with request status updated to cancelled

        Examples:
            | username | password |
            | smith    | pass1234 |

    Scenario Outline: Manager should be able to view all requests
        Given I am on manager login page
        When I input a valid username <username>
        When I input a valid password <password>
        When I click on the Submit button
        Then I should be on the page with title Manager account page
        When I click on manager view all requests
        Then I am on manager view all request page

        Examples:
            | username | password |
            | smith    | pass1234 |

Scenario Outline: Manager should be able to view accept requests
        Given I am on manager login page
        When I input a valid username <username>
        When I input a valid password <password>
        When I click on the Submit button
        Then I should be on the page with title Manager account page
        When I click on manager view accepted requests
        Then I am on manager view accepted request page

        Examples:
            | username | password |
            | smith    | pass1234 |

    Scenario Outline: Manager should be able to view reject requests
        Given I am on manager login page
        When I input a valid username <username>
        When I input a valid password <password>
        When I click on the Submit button
        Then I should be on the page with title Manager account page
        When I click on manager view rejected requests
        Then I am on manager view rejected request page

        Examples:
            | username | password |
            | smith    | pass1234 |
