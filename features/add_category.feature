@category
Feature: User adding a category
As a logged User
I should be able to add a new category for tasks

    Scenario: Adding a category with unique name
     Given there are no users 
     And there is a user named 'user1' with password 'pass1' and email 'user2@mail.com'
     And I am logged as 'user1' with password 'pass1'
     When I click the menu button
     And I put 'test' into name field on category form
     And I press submit button on category form
     Then there should be a category named 'test'

    Scenario: Adding a category with empty name
     Given there are no users 
     And there are no categories 
     And there is a user named 'user1' with password 'pass1' and email 'user2@mail.com'
     And I am logged as 'user1' with password 'pass1'
     When I click the menu button
     And I press submit button on category form
     Then there should be no categories

    Scenario: Adding a category with existing name
     Given there are no users 
     And there is a user named 'user1' with password 'pass1' and email 'user2@mail.com'
     And there is a category named 'cat1' for user 'user1'
     And I am logged as 'user1' with password 'pass1'
     When I click the menu button
     And I put 'cat1' into name field on category form
     And I press submit button on category form
     Then there should be a category named 'cat1'
