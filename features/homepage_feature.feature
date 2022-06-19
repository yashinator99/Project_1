Feature:users who go onto the homepage should be able to click on the login link

    Scenario:user clicks on the employee login link
        Given I am on the homepage
        When I click on the employee login link
        Then I should be routed to the employee login page



    Scenario:user clicks on the manager login link
        Given I am on the homepage
        When I click on the manager login link
        Then I should be routed to the manager login page




