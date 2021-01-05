# Social Gaming Project
## Contents
* [Brief](#brief)
    * [Requirements](#requirements)
    * [My Approach](#my-approach)
* [Architecture](#architecture)
    * [Database Layout](#database-layout)
    * [CI Pipeline](#ci-pipeline)
* [Project Tracking](#project-tracking)
* [Risk Assessment](#risk-assessment)
    * [Initial Risk Assessment](#initial-risk-assessment)
    * [Updated Risk Assessment](#updated-risk-assessment)
* [Testing](#testing)
    * [Unit Test](#unit-test)
    * [Integration Test](#integrartion-test)
* [Front-End Design](#front-end-design)
* [Known Issues](#known-issues)
* [Future Improvements](#future-improvements)
* [Authors](#authors)

## Brief

The main objective of this project is to make a web-based application that utilises create, read, update and delete functions through tools and technologies that uses all the core modules that we have learned over the past few weeks.

### Requirements

To achieve the objective of the project, I aim to include the following:
* A Trello Board
* A relational database which contains at least two tables that model a relationship
* Clear documentation of the design phase, app architecture, testing and risk assessment
* A python-based functional web application that optimises practices and design principles
* Unit testing and integration testing for the application
* A front-end website, created using Flask
* Code integrated into a Version Control System which will be built through a Jenkins CI Server and deployed to a cloud-based virtual machines

### My Approach

For this project, I have decided to produce a social gaming application that must allow the user to do the following:
* Add a new game (satisfies ‘Create’) that stores:
	* *Name of the Game*
	* *Number of Platforms*
	* *Genre*
* Add a rating for the games (satisfies ‘Create’) that stores:
	* *Name of game*
	* *Numbered rating of the game out of 5*
	* *Review of the game*
	* *Author/Username of review post*
* View and delete games (satisfies ‘Read’ and ‘Delete’)
* View, update and delete their review (satisfies ‘Read’, ‘Update’ and ‘Delete’)
* Search for reviews on certain games (Satisfies ‘Read’)

Additionally, I would like the user to:
* Add games to a portfolio, which consists of games that users have played and their reviews of the game
* Add a wishlist, which consists of games that users would like to purchase in the future

## Architecture

### Database Structure

Displayed below are the Entity-Relationship Diagrams (ERD) showing the structure of the database which will be implemented into the code.

>![ERD1][erd1]
>
> *Figure 1: Initial Entity-Relationship Diagram (ERD)*

The initial ERD (Figure 1) shows the original structure of the database. Initially, there was going to be a platform and genre table which connected from the games table. The platform table would have had a one-to-many relationship, as there can be many games in platforms. Also, the genre table would have been connected to the games table. 


>![ERD2][erd2]
>
> *Figure 2: Final Entity-Relationship Diagram (ERD)*

The ERD used in the final product as shown in figure 2. As displayed in the image, it can be seen that the ‘Games’ and ‘Ratings’ table has been implemented, whereas the ‘Wishlist’, ‘Portfolio’ and ‘User’ tables have not been implemented.  

The two relational tables that are used in the application are the ‘Games’ and ‘Ratings’ table. These are connected by a many-to-many-relationship. The reason they are connected by this relationship is because you can have zero-to-many ratings for a game and you can have one-to-many games for a rating. This is ideal because it hits the criteria to have two relational tables in a database. 

### CI Pipeline

>![cipipeline][ci-pip]
>
> *Figure 3: CI Pipeline Diagram*

Figure 3 shows the continuous integration pipeline that is connected with the associated tools and services used within the structure. Having this pipeline allows for a quick and easy development-to-deployment, as this allows automation of the integration process. This means that I am able to change code on my local machine or on my virtual machine and push the code to the GitHub repository, thus causing Jenkins to react to the webhook allowing it to be automatically installed onto the cloud virtual machine. Also, ‘pytest’ is automatically installed onto the server allowing us to test and run the coverage reports which show us if the code is working.

The Jenkins build consists of implementing in the GitHub repository, which triggers the ‘GitHub hook trigger’. The build executes the ‘startup’ script which comes from the repository this allows me to change the ‘startup’ script which triggers the build to start. The startup script contains the installation of Python and other requirements needed for the web application. Once this is all built by Jenkins, it runs the web application successfully and allows the user to use the app. 

## Project Tracking
The project tracking of this project was done by using Trello. You can find the link to the board used here: https://trello.com/b/O7BPhn7r/social-gaming-project
>![trello][tboard]
>
> *Figure 4: Trello Board for Social Gaming Project*

The Trello board has been designed such that tasks are moved from left to right. Each card is labelled with a colour which displays the parts of the project they are applied to. The boards displayed are listed as follows: 
* Product Backlog: These cards are a list of items that are needed to be completed for the project. 
* User Stories: These cards are lists of user stories that show the functionalities of the application. 
* Planning: These cards are a list of features that could have been included into the project and are in the ‘planning’ phase. 
* In progress: These cards are lists of items currently being worked on. 
* Testing: These cards are a list of items that are being tested.
* Finished: These cards are lists of processes that have been completed.

## Risk Assessment
### Initial Risk Assessment
Displayed below (Figure 5) is the initial risk assessment which shows the risks associated and assumed before making the web application.
>![initialrisk][irisk]
>
> *Figure 5: Initial Risk Assessment*
### Updated Risk Assessment
The updated risk assessment can be found here: https://docs.google.com/spreadsheets/d/1K0oOe0WRTf1r99D3WdDTF6l_0dBxpTVbylfzUqmbzY0/edit?usp=sharing

Displayed below (Figure 6) is the updated risk assessment which was made after the project was completed.
>![updatedrisk][urisk]
>
> *Figure 6: Updated Risk Assessment*

## Testing
### Unit Test
Unit testing is a functional type of testing, this means that if a feature of the website is used it will test the action is performed correctly. This is done by testing individual units of source code using various tests to determine if they are fit for use. 

The ‘pytest’ coverage mechanism shows us that all of the source code is being tested effectively. In Figure 7, you can see that the unit test for the source code has achieved 100% coverage. The picture below also shows a Jenkins build which is producing a console output that shows the developer the number of tests that have passed or failed in the code. 
>![pytestcov][cov]
>
> *Figure 7: Pytest - Unit Test Coverage*
### Integration Test
Integration testing is also a functional type of testing. It is the testing of multiple components of the application to cheque that they work together. Integration testing requires the developer to act like a consumer or user of the application and also shows if the end goal is reached by the function of a submit button in this instance. As shown in Figure 8, the integration testing is displayed as ‘test_int.py’. 
>![inttest][integ]
>
> *Figure 8: Pytest - Integration Test*

## Front-End Design
The Front-End design is very basic at the minute, as it is built with simple HTML. Even though this is the case, it is still functional and works within reason. 

The ‘home page’ below is the first URL seen by the user. 
>![home][homepage]
>
> *Figure 9: Home Page*

The ‘game page’ URL chose all of the games in the database as well as the ratings associated with each game. 
>![game][gamepage]
>
> *Figure 10: Game Page*

The ‘add game’ URL allows the user to add a new game into the database. 
>![addgame][addgame]
>
> *Figure 11: Add Game Page*

The ‘show rating’ URL allows the user to see the rating of a game from the list of games of where they have clicked a button to be redirected to this URL. 
>![showrating][showrating]
>
> *Figure 12: Show Rating Page*

The ‘rating’ URL allows the user to choose between adding a new review or searching an old review. 
>![rating][rating]
>
> *Figure 13: Rating Page*

The ‘search rating’ URL allows the user to search for a rating for a specific game. 
>![search][searchrating]
>
> *Figure 14: Search Rating Page*

The ‘add rating’ URL allows the user to add a new rating to a game of their choice. 
>![addrating][addrating]
>
> *Figure 15: Add Rating Page*

The ‘update review’ URL allows the user to update a review of a specific review they have chosen before. 
>![updaterev][updaterev]
>
> *Figure 16: Update Rating Page*
## Known Issues
The bugs in the system are listed below:
* Entering a form field with a phrase that isn't in the database will cause an Attribute Error.


## Future Improvements
There are a number of improvements I would like to add to this application that would be beneficial:
* Make the Web application look better by using Bootstrap CSS or other CSS libraries. 
* Include a validation which stops the user from entering multiple reviews for one game, so that they can only update their review through the ‘update review’ URL. 
* Add extra features into the web application such as a portfolio, which allows the user to add the games they have played and a review for those games this would then link into the ratings table. 
* Add a feature for a wish list, which shows prices of the games wanted by the user.
* Add user logins into the applicaiton.
## Authors
Naserul Islam

[erd1]: https://imgur.com/XzTXPzK.png
[erd2]: https://imgur.com/Cxgs7oy.png
[ci-pip]: https://imgur.com/Utv5RPp.png
[tboard]: https://imgur.com/RT0KHAd.png
[irisk]: https://imgur.com/rvZvX9Q.png
[urisk]: https://imgur.com/Dak7Mhp.png
[cov]: https://imgur.com/TiI9psx.png
[integ]: https://i.imgur.com/qgkzv5g.png
[homepage]: https://imgur.com/3v3sLaB.png
[gamepage]: https://imgur.com/juE1bBF.png
[addgame]: https://i.imgur.com/nQksAON.png
[showrating]: https://i.imgur.com/kC67ifA.png
[rating]: https://i.imgur.com/sOgle6A.png
[searchrating]: https://i.imgur.com/vNCmB4t.png
[addrating]: https://i.imgur.com/klyb8Pp.png
[updaterev]: https://i.imgur.com/DeaK4hz.png
