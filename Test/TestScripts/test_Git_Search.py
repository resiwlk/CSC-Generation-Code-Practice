import sys

from Src.Environment.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.Git_HomePage import Git_HomePage
from Src.PageObject.Pages.Git_SearchPage import Git_SearchPage
from Src.PageObject.Pages.Git_AdvancedSearchPage import Git_AdvancedSearchPage
from Src.PageObject.Pages.Git_MvoloskovRepoPage import Git_MvoloskovRepoPage
from selenium.webdriver.common.by import By

import unittest
from selenium import webdriver
from time import sleep
 
class test_Git_Search (WebDriverSetup):
 
    def test_git_search(self):
        driver = self.driver
        self.driver.get("https://github.com/")
        self.driver.set_page_load_timeout(30)
        
        #Verifiy at Git Home Page
        
        web_page_title = "GitHub: Where the world builds software · GitHub"
        if driver.title == web_page_title:
            print("Git Homoe Page loaded successfully")
        self.assertEqual(driver.title,web_page_title)
        
        #Search "react" repository
        git_home_page = Git_HomePage(driver)
        git_home_page.search_project("react")
        sleep(5)
        
        #Verify at Repisitory Search Page
        web_page_title = "Search · react · GitHub"
        if driver.title == web_page_title:
            print("Search \"react\" page loaded successfully")
        self.assertEqual(driver.title,web_page_title)
        
        #Click "Advanced Search" Link
        git_search_page = Git_SearchPage(driver)
        git_search_page.click_advanced_search();
        sleep(5)
        
        #Verify at "Advanced Search" page
        web_page_title = "GitHub · Where software is built"
        if driver.title == web_page_title:
            print("Advanced Search \"react\" page loaded successfully")
        self.assertEqual(driver.title,web_page_title)
        
        #Set the Advanced Search criteria:  
        #- Written in this language: JavaScript;
        #- With this many stars: >45;
        #- With this many followers: >50;
        #- With this license: Boost Software License 1.0;
        git_advanced_search_page = Git_AdvancedSearchPage(driver)
        git_advanced_search_page.select_language("JavaScript")
        sleep(1)
        git_advanced_search_page.input_number_of_stars(">45")
        sleep(1)
        git_advanced_search_page.input_number_of_followers(">50")
        sleep(1)
        git_advanced_search_page.select_license("Boost Software License 1.0")
        sleep(1)
        git_advanced_search_page.search()
        sleep(5)
        
        #Reload the Repisitory Search Page， Check if there is only 1 repositroy and if the mvoloskov/decider is in the list
        git_search_page = Git_SearchPage(driver)
        web_page_title = "Search · react stars:>45 followers:>50 language:JavaScript license:bsl-1.0 · GitHub"
        if driver.title == web_page_title:
            print("Search \"react\" page loaded successfully")
        self.assertEqual(driver.title,web_page_title)
        
        if(git_search_page.get_number_of_repositories()=="1"):
            print("Only 1 repository identfied based on the advanced search criteria")
        self.assertEqual(git_search_page.get_number_of_repositories(),"1")
        
        if(git_search_page.get_first_repository_name()=="mvoloskov/decider"):
            print("Repository \"mvoloskov/decider\" is listed.")
        self.assertEqual(git_search_page.get_first_repository_name(),"mvoloskov/decider")
        
        #Click the mvoloskov/decider repository
        git_search_page.click_first_repository_link();
        sleep(5)
        
        #Verify at mvoloskov/decider repository page
        web_page_title = "GitHub - mvoloskov/decider: 🤔 Apply CSS to React components conditionally"
        if driver.title == web_page_title:
            print("Repository \"mvoloskov/decider\" page loaded successfully")
        self.assertEqual(driver.title,web_page_title)
        
        #Naviagate to ReadMe file
        git_repository_page = Git_MvoloskovRepoPage(driver)
        git_repository_page.click_readme_link();
        sleep(5)
        
        #Verify ReadMe File is loaded. Click the Raw button to show the raw data of the ReadMe file
        web_page_title = "decider/README.md at master · mvoloskov/decider · GitHub"
        if driver.title == web_page_title:
            print("ReadMe file loaded successfully")
        self.assertEqual(driver.title,web_page_title)
        git_repository_page = Git_MvoloskovRepoPage(driver)
        git_repository_page = Git_MvoloskovRepoPage(driver)
        git_repository_page.click_raw_link();
        sleep(5)
        
        #Print the first 300 characters of the [README.md]
        print("the first 300 characters of the [README.md] is :")   
        print("---------------------------------------------------")         
        result=driver.find_element(By.XPATH, "/html/body/pre").text
        print(result[0:300])
        print("---------------------------------------------------") 
        
        
if __name__ == '__main__':
    unittest.main()