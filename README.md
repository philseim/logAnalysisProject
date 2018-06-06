# Log Anlaysis Project for Udacity

## About

This is my submission for the Movie project for the Udacity Nano degree. 
It reports on the three questions  by the course.
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

The output shows the answers in the terminal and creates a txt file in the same directory of the python file that has the results.

## Prerequisites for running the programme
- Python v 3.x
- Git Bash or similiar terminal system
- VirtualBox: https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
- vagrant: https://www.vagrantup.com/downloads.html
- VM config from Udacity: https://github.com/udacity/fullstack-nanodegree-vm
- newsdata.sql downloaded from: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

## Running the Programme
1. Start the virtual machine by running the command in git bash `vagrant up` after cd'ing into the vagrant subdirectory
2. Copy the files into a directory called logAnalysisProject or clone the directory into the **vagrant folder**
3. Put the newsdata.sql file into the vagrant directory
4. Log in to the VM by running the command `vagrant ssh` from git bash  
4. Run the following command: cd /vagrant/logAnalysisProject to get into the directory where the python file is stored
5. Run the file PythonConnect.py to run the programme
6. A file will be created in the same directory called "testfile.txt" which will contain the results

## Note
All the files need to be in the same folder or the programme will not run correctly.