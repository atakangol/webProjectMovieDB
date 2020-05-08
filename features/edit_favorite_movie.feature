Feature: Edit Movie
  In order to keep updated my previous registers about movies
  As a user
  I want to edit a movie register I created

  Background: There are registered users and a movie by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists movie registered by "user1"
      | movieName       | Pname             |
      | Joker           | Joaquim Phoenix   |

  Scenario: Edit owned movie
    Given I login as user "user1" with password "password"
    When I edit the actor with name "Joaquim Phoenix"
      | pName           |
      | Joaquim Phoenix |
    Then I'm viewing the details page for movies by "user1"
      | movieName       | Pname             |
      | Joker           | Joaquim Phoenix   |
    And There are 1 movies

  Scenario: Try to edit movie but not logged in
    Given I'm not logged in
    When I view the details for movies "Joker"
    Then There is no "edit" link available

