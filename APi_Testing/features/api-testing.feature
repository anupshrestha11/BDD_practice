Feature: Test CRUD methods in sample REST API testing framework

  Background:
    Given I set sample REST API url

  Scenario: POST posts example
    Given I set POST posts api endpoint
    When I set HEADER param request content type as "application/json."
    And Set request Body
    And Send a POST HTTP request
    Then I receive valid HTTP response code 201
    And Response BODY "POST" is non-empty.

  Scenario: GET posts example
    Given I set GET posts api endpoint
    When I set HEADER param request content type as "application/json."
    And Send a GET HTTP request
    Then I receive valid HTTP response code 200
    And Response BODY "GET" is non-empty.


  Scenario: UPDATE posts example
    Given I set PUT posts api endpoint for "1"
    When I set Update request Body
    And Send PUT HTTP request
    Then I receive valid HTTP response code 200 for "PUT"
    And Response BODY "PUT" is non-empty.

  Scenario: DELETE posts example
    Given I set DELETE posts api endpoint for "1"
    When Send DELETE HTTP request
    Then I receive valid HTTP response code 200 for "DELETE"

