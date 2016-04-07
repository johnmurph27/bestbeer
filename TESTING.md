TESTING
=======

Who: List of people on the team
-----------
* Andrew Lim
* Ryan Matthews
* Juan Carlos Herrera
* John Murphy
* Charlie Luckhart

Title: of project
-----------
* Best Beer

Vision: from Project Part 1 Proposal
-----------
* Vision Statement: "The perfect beer for you"
* Motivation: We want good beer

Automated Tests: Testing scraper and MySQL Database
-----------
### Test 1 - Scraper
* Ryan
### Test 2 - MySQL
* To automatically test our PHP­to­mysql interface, we used the unit testing framework PHPUnit ( https://phpunit.de/ ). Running the tests requires inserting the test sql data from our TADatabase.sql (being careful that your sql server matches up with to_json.php in terms of password and the name of the database) and then simply running ‘phpunit to_json_test.php’. Naturally, PHP (specifically PHP 5.6) and PHPUnit must be properly installed before the tests will run­­instructions to install both can be found in the top comments of to_json.php and to_json_test.php. The test file currently tests all the functions from to_json.php, and all tests currently pass with the occasional exception caused by the SQL server’s data being altered from its initial state by a broken test, which requires the server to be reset to the data from TADatabase.sql in order for the test to pass again (running the tests immediately after using TADatabase.sql as the source and not altering any of the sql data should not avoid this program).

User Acceptance Tests: Copy of at least three UAT plans
-----------
