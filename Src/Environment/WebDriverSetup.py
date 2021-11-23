import unittest
from selenium import webdriver
import time
from time import sleep
import warnings
import urllib3
 
class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
 
    def tearDown(self):
        if (self.driver != None):
            print("Clean test environment. Exit all existing web driers.")
            self.driver.close()
            self.driver.quit()