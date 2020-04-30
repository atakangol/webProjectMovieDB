Feature: Register Favorite Movie
In order to know the user favorite movies,
As a user
I want to register the favorite movies whit its name.

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register just movie name
    Given I login as user "user" with password "password"
    When I register restaurant
      | name        |
      | The Tavern  |
    Then I'm viewing the details page for restaurant by "user"
      | name        |
      | The Tavern  |
    And There are 1 movies