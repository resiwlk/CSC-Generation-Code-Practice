import sys
import os

 
from selenium.webdriver.common.by import By
from Src.PageObject.Locators import Git_Locator
 
class Git_SearchPage(object):
    def __init__(self, driver):
 
        self.driver = driver
        self.git_advanced_search_link = driver.find_element_by_link_text(Git_Locator.Git_Advanced_Search_Link)
        self.git_number_of_repository = driver.find_element(By.XPATH, Git_Locator.Git_Number_Of_Repository)
        self.git_first_repository_link = driver.find_element(By.XPATH, Git_Locator.Git_First_Repository_Link)

    def get_git_advanced_search_link(self):
        return self.git_advanced_search_link
    
    def get_git_number_of_repository(self):
        return self.git_number_of_repository    

    def get_git_first_repository_link(self):
        return self.git_first_repository_link  
        
    def click_advanced_search(self):
        self.git_advanced_search_link.click()
    
    def get_number_of_repositories(self):
        result=self.git_number_of_repository.text.split()[0]
        return result
        
    def get_first_repository_name(self):
        return self.git_first_repository_link.text
    
    def click_first_repository_link(self):
        self.git_first_repository_link.click()