class Git_Locator(object):
#Locators for Git Home Page
    Git_Search_Bar = "//input[@name='q']"
    
#Locators for Git search Page
    Git_Advanced_Search_Link = "Advanced search"   #Link name, not XPath
    Git_Number_Of_Repository = "//*[@id='js-pjax-container']/div/div[3]/div/div[2]/h3"
    Git_First_Repository_Link = "//*[@id='js-pjax-container']/div/div[3]/div/ul/li/div[2]/div[1]/div[1]/a"
    
 
#Locators for Git advanced search Page 
    Git_Advanced_Search_Language = "//*[@id='search_language']"
    Git_Advanced_Search_Stars = "//*[@id='search_stars']"
    Git_Advanced_Search_Followers = "//*[@id='search_followers']"
    Git_Advanced_Search_License = "//*[@id='search_license']"
    Git_Advanced_Search_Button = "//*[@id='search_form']/div[2]/div/div/button"
    
 
#Locators for mvoloskov/decider page
    Git_ReadMe_Link = "README.md"  #Link name, not XPath
    Git_Raw_Link = "Raw" #Link name, not XPath