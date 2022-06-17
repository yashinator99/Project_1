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