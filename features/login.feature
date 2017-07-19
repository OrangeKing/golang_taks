@login
Feature: User logging in
As a User
I should be able to log in to my account

    Scenario: Logging with registered user credentials
     Given there are no users
     And there is a user named 'user1' with password 'pass1' and email 'user2@mail.com'
     When I go to the landing page
     And I put 'user1' into 'username' field on login form
     And I put 'pass1' into 'password' field on login form
     And I press submit button on login form
     Then I should be logged in

    Scenario: Logging as non-existent user
     Given there are no users
     When I go to the landing page
     And I put 'user1' into 'username' field on login form
     And I put 'pass1' into 'password' field on login form
     And I press submit button on login form
     Then I should be at the landing page

    Scenario: Login with wrong password 
     Given there are no users
     And there is a user named 'user1' with password 'pass2' and email 'user2@mail.com'
     When I go to the landing page
     And I put 'testuser' into 'username' field on login form
     And I put 'wrongpassword' into 'password' field on login form
     And I press submit button on login form
     Then I should be at the landing page
