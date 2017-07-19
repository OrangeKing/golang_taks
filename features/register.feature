@register
Feature: New user registration
As a User
I should be able to create new account

   Scenario: Create a new user with unique name
    Given there are no users 
    When I go to the landing page
    And I put 'testuser' into 'username' field on sign up form
    And I put 'testpassword' into 'password' field on sign up form
    And I put 'testuser@mail.com' into 'email' field on sign up form
    And I press submit button on sign up form
    Then there should be user named 'testuser' with password 'testpassword' and email 'test@test.com'
    
    Scenario: Create user with empty password
     Given there are no users
     When I go to the landing page
     And I put 'user1' into 'username' field on sign up form
     And I put 'user@mail.com' into 'email' field on sign up form
     And I press submit button on sign up form
     Then there should be no user named 'user1'

    Scenario: Create user with duplicate name
     Given there are no users
     And there is a user named 'user1' with password 'pass2' and email 'user2@mail.com'
     When I put 'user1' into 'username' field on sign up form
     And I put 'pass1' into 'password' field on sign up form
     And I put 'user@mail.com' into 'email' field on sign up form
     And I press submit button on sign up form
     Then there should be user named 'user1' with password 'pass2' and email 'user2@mail.com'
