Feature: List Favorite Movies
In order to keep myself up to date about favorite movies,
As a user
I want to list my favorite movies.

Background: There are 4 registered movies by same user
    Given Exists a user "user" with password "password"
    And Exists movie registered by "user"
      | movieName       | Pname             | user  |
      | Joker           | Joaquim Phoenix   | user  |
      | Titanic         | Leonardo Dicaprio | user  |
      | Venganza        | Liam Neeson       | user  |
      | El Camino       | Aaron Paul        | user  |

  Scenario: List the last four
    When I list movies
    Then I'm viewing a list containing
      | movieName       | Pname             | user  |
      | Joker           | Joaquim Phoenix   | user  |
      | Titanic         | Leonardo Dicaprio | user  |
      | Venganza        | Liam Neeson       | user  |
      | El Camino       | Aaron Paul        | user  |
    And The list contains 4 movies

#  Scenario: List the last four
#    Given Exists movie registered by "user"
#      | movieName       | favoriteCharacter |
#      | Pretty Woman    | Richard Gere      |
#    When I list movies
#    Then I'm viewing a list containing
#      | movieName       |
#      | Pretty Woman    |
#      | El Camino       |
#      | Venganza        |
#      | Titanic         |
#    And The list contains 4 movies