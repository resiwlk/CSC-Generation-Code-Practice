import sys
import os

 
from selenium.webdriver.common.by import By
from Src.PageObject.Locators import Git_Locator
from selenium.webdriver.support.ui import Select
 
class Git_AdvancedSearchPage(object):
    def __init__(self, driver):
 
        self.driver = driver      
        self.advanced_search_language = driver.find_element(By.XPATH, Git_Locator.Git_Advanced_Search_Language)
        self.advanced_search_stars = driver.find_element(By.XPATH, Git_Locator.Git_Advanced_Search_Stars)
        self.advanced_search_followers = driver.find_element(By.XPATH, Git_Locator.Git_Advanced_Search_Followers)
        self.advanced_search_license = driver.find_element(By.XPATH, Git_Locator.Git_Advanced_Search_License)
        self.advanced_search_button = driver.find_element(By.XPATH, Git_Locator.Git_Advanced_Search_Button)
        
        
    def get_advanced_search_language(self):
        return self.advanced_search_language
 
    def get_advanced_search_stars(self):
        return self.advanced_search_stars

    def get_advanced_search_followers(self):
        return self.advanced_search_followers

    def get_advanced_search_license(self):
        return self.advanced_search_license

    def get_advanced_search_button(self):
        return self.advanced_search_button      
        
    def select_language(self,language):
        select = Select(self.advanced_search_language)
        select.select_by_visible_text(language)
    
    def input_number_of_stars(self,stars):
        self.advanced_search_stars.send_keys(stars);
    
    def input_number_of_followers(self,followers):
        self.advanced_search_followers.send_keys(followers);
    
    def select_license(self,license):
        select = Select(self.advanced_search_license)
        select.select_by_visible_text(license)
        
    def search(self):
        self.advanced_search_button.click()