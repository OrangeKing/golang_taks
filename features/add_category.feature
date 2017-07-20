@category
Feature: User adding a category
As a logged User
I should be able to add a new category for tasks

    Scenario: Adding a category with unique name
     Given there are no users 
     And there is a user named 'user1' with password 'pass1' and email 'user2@mail.com'
     And I am logged as 'user1' with password 'pass1'
     When I click the menu button
     And I put 'test' into 'name' field on category form
     And I press submit button on category form
     Then A new category named 'test' should be created
