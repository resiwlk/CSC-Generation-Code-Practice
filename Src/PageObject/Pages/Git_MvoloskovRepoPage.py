import sys
import os

from selenium.webdriver.common.by import By
from Src.PageObject.Locators import Git_Locator
 
class Git_MvoloskovRepoPage(object):
    def __init__(self, driver):
        self.driver = driver
        
    def click_readme_link(self):
        self.driver.find_element_by_link_text(Git_Locator.Git_ReadMe_Link).click()
    
    def click_raw_link(self):
        self.driver.find_element_by_link_text(Git_Locator.Git_Raw_Link).click()
        