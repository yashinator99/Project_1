Feature: Users who logon should be able to make reimbursement requests

    Scenario Outline: User should be able to make requests
        Given emp user1 on login page
        When emp user1 inputs username <username>
        When emp user1 inputs password <password>
        When emp user1 clicks submit on login page
        Then emp user1 is on account page
        When emp user1 clicks on request reimbursement
        Then emp user1 is on request reimbursement page
        When emp user1 inputs request description <desc>
        When emp user1 inputs request amount <amount>
        When emp user1 clicks submit on request reimbursement page
        Then emp user1 should be back on account page

        Examples:
            | username | password | desc      | amount |
            | billy    | pass1234 | testdesc2 | 100    |

    Scenario Outline: Managers should be able to make requests
        Given I am on manager login page
        When I input a valid username <username>
        When I input a valid password <password>
        When I click on the Submit button
        Then I should be on the page with title Manager account page
        When I click on request reimbursement
        Then I am on request reimbursement page
        When I input request description <desc>
        When I input request amount <amount>
        When I click submit on request reimbursement page
        Then I should be back on account page

        Examples:
            | username | password | desc      | amount |
            | smith    | pass1234 | test3     | 200    |

    Scenario Outline: Managers should be able to make requests 2
        Given I am on manager login page
        When I input a valid username <username>
        When I input a valid password <password>
        When I click on the Submit button
        Then I should be on the page with title Manager account page
        When I click on request reimbursement
        Then I am on request reimbursement page
        When I input request description <desc>
        When I input request amount <amount>
        When I click submit on request reimbursement page
        Then I should be back on account page

        Examples:
            | username | password | desc      | amount |
            | smith    | pass1234 | test4     | 340    |