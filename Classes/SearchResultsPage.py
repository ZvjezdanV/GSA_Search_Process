
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from Classes.Selenium_WebDriver import WebDriver


class SearchResultsPage(WebDriver):
    """This is the page that's associated to our Search Results Page"""
    
    def __init__(self, object: ChromeWebDriver):
        self.chrome_driver = object
        self.__verify_page_load()
    
                
    # Private Method           
    def __verify_page_load(self):
        self.wait_displayed("//form[@id='searchResultsID']//h2[contains(text(), 'Search Terms:')]")
        self.wait_displayed("//form[@id='searchResultsID']//input[@type='submit' and @title='Clear Search']")