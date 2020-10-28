
from typing import Optional
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from Classes.Selenium_WebDriver import WebDriver
from selenium.webdriver.common.by import By
from Classes.SearchRecordsPage import SearchRecordsPage


class LandingPage(WebDriver):
    """This is the landing page that's associated to our GSA Site"""
    
    def __init__(self, object: Optional[ChromeWebDriver]):
        if object != None:
            self.chrome_driver = object
            self.__verify_page_load()
        else:
            self.chrome_driver = WebDriver().chrome_driver
            self.chrome_driver.get("https://www.sam.gov/SAM/")
            self.__verify_page_load()
    
                
    # Private Method           
    def __verify_page_load(self):
        self.wait_displayed("//form[@id='searchForm']//a[@title='Search Records']")
        self.wait_displayed("//div[@id='samContentForm']//p[contains(text(), 'System for Award Management (SAM)')]")
        
    
    def click_search_records(self):
        self.chrome_driver.find_element(By.XPATH, "//form[@id='searchForm']//a[@title='Search Records']").click()
        return SearchRecordsPage(self.chrome_driver)