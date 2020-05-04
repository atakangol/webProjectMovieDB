Feature: List Favorite Movies
In order to keep myself up to date about favorite movies,
As a user
I want to list my favorite movies.

Background: There are 4 registered movies by same user
    Given Exists a user "user" with password "password"
    And Exists movie registered by "user"
      | movieName       | favoriteCharacter |
      | Joker           | Joaquim Phoenix   |
      | Titanic         | Leonardo DiCaprio |
      | Venganza        | Liam Neeson       |
      | El Camino       | Aaron Paul        |

  Scenario: List the last four
    When I list movies
    Then I'm viewing a list containing
      | movieName       |
      | Joker           |
      | Titanic         |
      | Venganza        |
      | El Camino       |
    And The list contains 5 restaurants

  Scenario: List the last four
    Given Exists movie registered by "user"
      | movieName       | favoriteCharacter |
      | Pretty Woman    | Richard Gere      |
    When I list movies
    Then I'm viewing a list containing
      | movieName       |
      | Pretty Woman    |
      | El Camino       |
      | Venganza        |
      | Titanic         |
    And The list contains 4 movies