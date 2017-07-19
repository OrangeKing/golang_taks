@logout
Feature: User logging out
As a logged User
I should be able to log out to my account

    Scenario: Logging with registered user credentials
     Given there are no users 
     And there is a user named 'user1' with password 'pass1' and email 'user2@mail.com'
     And I am logged as 'user1' with password 'pass1'
     When I click the logout button
     Then I should be logged out
     And I should be at the landing page
