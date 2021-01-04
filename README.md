# Social Gaming Project
> ## To Do List:
> * Risk Assessment
> * ER Diagram
> * Trello Board
> * Databases
> * Flask Application
> * Markdown
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

## Risk Assessment
### Initial Risk Assessment
### Updated Risk Assessment

## Testing
## Authors
Naserul Islam

[erd1]: https://imgur.com/XzTXPzK.png
[erd2]: https://imgur.com/Cxgs7oy.png
[ci-pip]: https://imgur.com/Utv5RPp.png
[tboard]: https://imgur.com/RT0KHAd.png