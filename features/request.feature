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