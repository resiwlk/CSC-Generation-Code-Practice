# Code Practice: CSC Generation - QA Automation Engineer  

## Overview
- Applied Page Object Model in this project
- Use Unittest as the test execution framework
- Moving all the locators for the elements to a seperate file for better maintainability
- Implemented and Tested under Chrome 96.0 with corresponding Chrome webdriver

## Execution
- Install Selenium (pip install Selenium)
- Install testtools (pip install testtools)    *（optional)*  
- Navigate to the root path (i.e. where ReadMe.md file locate)
- Run /Test/Execution/TestRunner.py

## Scripts explanation
- Resource: I have attached the [ChromeDriver 96.0.4664.45] in the Resource Folder (https://chromedriver.storage.googleapis.com/index.html?path=96.0.4664.45/)
- Src:
	- Environment: 
		- WebDriverSetup.py : To manage all the web drivers. Currently I only implemented Chrome webdriver
	- PageObject:
		- Pages: Contains the definition for all visited web pages 
			- Git_AdvancedSearchPage.py
			- Git_HomePage.py
			- Git_MvoloskovRepoPage.py
			- Git_SearchPage.py
		- Locators: Contains the locater for all used web elements.
- Test
	-  Execution:
		- TestRunner.py : Entry point, as well as where we manage the test executions, including what to be executed, in what order, etc.
	- TestScripts: All the test case scripts. Currently since we only have one case there is only one script
		- test_Git_Search.py
