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

Below is an entity-relationship diagram (ERD) showing the structure of the database. 


![ERD][erd1]
> Entity-Relationship Diagram


![cipipeline][ci-pip]
> CI Pipeline Diagram
## Authors
Naserul Islam

[erd1]: https://imgur.com/WykpT4C.png
[ci-pip]: https://imgur.com/R4Wv1ul.png
