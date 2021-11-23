import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Src.PageObject.Locators import Git_Locator
from time import sleep

 
class Git_HomePage(object):
    def __init__(self, driver):
 
        self.driver = driver
        self.search_bar = driver.find_element(By.XPATH, Git_Locator.Git_Search_Bar)
 
    def get_git_search_bar(self):
        return self.search_bar

    def search_project(self,search_content):
        self.search_bar.send_keys(search_content)
        sleep(2)
        self.search_bar.send_keys(Keys.RETURN)