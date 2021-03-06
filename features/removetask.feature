@task_remove
Feature: User removing a task
As a logged User
I should be able to remove previously created task

    Scenario: Removing a preexisting task
     Given there are no users 
     And there are no tasks
     And there is a user named 'user1' with password 'pass1' and email 'user2@mail.com'
     And there is a category named 'cat1' for user 'user1'
     And there is a task named 'task1' for user 'user1' in category 'cat1' with priority 'Low'
     And I am logged as 'user1' with password 'pass1'
     When I press the remove task button
     Then there should be deleted task 'task1' for user 'user1'
