@task_edit
Feature: User editing a task
As a logged User
I should be able to edit any task in specified category with specified priority

    Scenario: Editing a preexisting task with defined priority
     Given there are no users 
     And there are no categories
     And there are no tasks
     And there is a user named 'user1' with password 'pass1' and email 'user2@mail.com'
     And there is a category named 'cat1' for user 'user1'
     And there is a task named 'task1' for user 'user1' in category 'cat1' with priority 'Low'
     And I am logged as 'user1' with password 'pass1'
     When I press the modify task button
     And I select 'Medium' from priority field on task form
     And I press submit button on task form
     Then there should be a task named 'task1' for user 'user1' with priority 'Medium'
