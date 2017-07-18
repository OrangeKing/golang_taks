Feature: New user registration
As a User
I should be able to create new account

   Scenario: Create a new user with unique name
    Given there are no users 
    When I go to landing page
    Then I will see registration form

# Given there are no users
# When I go to the landing page
# And I put 'user1' into 'username' field on sign up form
# And I put 'pass1' into 'password' field on sign up form
# And I put 'user@mail.com' into 'email' field on sign up form
# And I press submit on sign up form
# Then there should be user named 'user1' with password 'pass1' and email 'user@mail.com'
