@task_add
Feature: User adding a task
As a logged User
I should be able to add a new task in specified category

    Scenario: Adding a task with unique name, defined category and priority
     Given there are no users 
     And there are no tasks
     And there is a user named 'user1' with password 'pass1' and email 'user2@mail.com'
     And there is a category named 'cat1' for user 'user1'
     And I am logged as 'user1' with password 'pass1'
     When I press the add task button
     And I put 'task1' into title field on task form
     And I select 'Low' from priority field on task form
     And I select 'cat1' from category list on task form
     And I press submit button on task form
     Then there should be a task named 'task1' for user 'user1'

    Scenario: Adding a task empty name
     Given there are no users 
     And there are no tasks
     And there is a user named 'user1' with password 'pass1' and email 'user2@mail.com'
     And there is a category named 'cat1' for user 'user1'
     And I am logged as 'user1' with password 'pass1'
     When I press the add task button
     And I select 'Low' from priority field on task form
     And I press submit button on task form
     Then there should be no tasks
