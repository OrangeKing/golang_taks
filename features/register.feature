Feature: New user registration
As a User
I should be able to create new account

   Scenario: Create a new user with unique name
    Given There are no users 
    When I go to landing page
    And I put 'testuser' into 'username' field on sign up form
    And I put 'testpassword' into 'password' field on sign up form
    And I put 'testuser' into 'email' field on sign up form
    And I press submit button on sign up form
    Then there should be user named 'testuser' with password 'testpassword' and email 'test@test.com'
