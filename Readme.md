# PROJECT : LOG-ANALYSIS
This project is a part of the **FULL STACK NANODEGREE** program from **UDACITY**.

## DESCRIPTION :
The purpose of this project is to create a reporting tool that will several
questions using the data from the database news.
This is done by creating a python code which connects to the database **news** and runs several queries on it to answer the following questions :
  * What are the most popular three articles of all time?
  * Who are the most popular article authors of all time?
  * On which days did more than 1% of requests lead to errors?

## Pre-Requisites :


  * **PYTHON** : Need atleast python 2.7 or a greater version.
 For downloading the latest version click [here](https://www.python.org/download/releases/3.0/)


  * **GIT** : It is a version control system (VCS) which tracks the file changes, commonly used for programming in a team setting. It can be downloaded from
  [here](https://git-scm.com/).


  * **VAGRANT** : Download and install vagrant from [here](https://www.vagrantup.com/downloads.html).
    You can configure vagrant on your machine by forking the repository :
    https://github.com/udacity/fullstack-nanodegree-vm.


 * **VIRTUALBOX** : This is a tool from oracle which enables you to run multiple
     operating systems simultaneously.
     It can be downloaded by clicking [here](https://www.virtualbox.org/)

## HOW TO RUN? :

*  Download the database file from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and copy the newsdata.sql file
into your vagrant directory.

* Using gitbash enter your vagrant directory and launch the virtual machine using the command : `$ vagrant up`

* Log in to your VM using the command : `$ vagrant ssh`

* Load the data from newsdata.sql into vagrant using the command :

  `psql -d news -f newsdata.sql`

* You can connect to the database using `psql -d news` and then run various commands on it.

* Run the python file using the command `python log-analysis.py`
 
