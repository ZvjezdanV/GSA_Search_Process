

from typing import Optional
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from Classes.Selenium_WebDriver import WebDriver
from selenium.webdriver.common.by import By
from Data.Doctor import Doctor
from Classes.SearchResultsPage import SearchResultsPage


class SearchRecordsPage(WebDriver):
    """This is the landing page that's associated to our Search Records Page"""
    
    def __init__(self, object: Optional[ChromeWebDriver]):
        if object != None:
            self.chrome_driver = object
            self.__verify_page_load()
        else:
            self.chrome_driver = WebDriver().chrome_driver
            self.chrome_driver.get("https://www.sam.gov/SAM/pages/public/searchRecords/search.jsf")
            self.__verify_page_load()
    
                
    # Private Method           
    def __verify_page_load(self):
        self.wait_displayed("//form[@id='searchForm']//a[@title='Search Records']")
        self.wait_displayed("//div[@id='samContentForm']//h2[text()='Search Tips to Get Started:']")
        self.wait_displayed("//input[@id='searchBasicForm:qterm_input']")
        
    
    def search_for_doctor(self, doctor : Doctor):
        self.chrome_driver.find_element(By.XPATH, "//input[@id='searchBasicForm:qterm_input']").send_keys(f'{doctor.firstName} {doctor.lastName}')
        self.chrome_driver.find_element(By.XPATH, "//form[@id='searchBasicForm']//input[contains(@id, 'SearchButton') and @title='Search']").click()
        return SearchResultsPage(self.chrome_driver)
        