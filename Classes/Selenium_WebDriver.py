
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as DriverWait
from selenium.webdriver.support import expected_conditions as DriverConditions


class WebDriver:
    """This is our class that uses our Selenium Chrome WebDriver"""
    
    def __init__(self):
        self.chrome_driver = self.__get_chrome_driver()
        
    # Private Method    
    def __get_chrome_driver(self):
        """This sets up our Chrome Driver and returns it as an object"""
        path_to_chrome = "F:\Selenium_Drivers\Windows_Chrome85_Driver\chromedriver.exe"
        self.chrome_options = webdriver.ChromeOptions() 
        self.chrome_options.add_argument("window-size=1500,1000")
        
        # Removes the "This is being controlled by automation" alert / notification
        self.chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        return webdriver.Chrome(executable_path = path_to_chrome,
                                options = self.chrome_options)
    
    
    def wait_displayed(self, xpath: str, int = 5):
        try:
            DriverWait(self.chrome_driver, int).until(
                DriverConditions.presence_of_element_located(locator = (By.XPATH, xpath))
            )
        except:
            raise WebDriverException(f'Timeout: Failed to find {xpath}')
        
        
    def is_displayed(self, xpath: str, int = 5):
        try:
            webElement = DriverWait(self.chrome_driver, int).until(
                DriverConditions.presence_of_element_located(locator = (By.XPATH, xpath))
            )
            
            return True if webElement != None else False
        except:
            return False
        
        
    def scroll_to_element(self, xpath : str, int = 5):
        try:
            webElement = DriverWait(self.chrome_driver, int).until(
                DriverConditions.presence_of_element_located(locator = (By.XPATH, xpath))
                )
            self.chrome_driver.execute_script("arguments[0].scrollIntoView();", webElement)
        except:
            raise WebDriverException(f'Timeout: Failed to find element using xpath {xpath}\nResult: Could not scroll')
        
        
    def is_element_populated(self, xpath : str, search_text : str):
        """Checks to see if our element has any Input Text"""
        for counter in range(10):
            webElement = self.chrome_driver.find_element(By.XPATH, xpath)
            if webElement.get_attribute('value').find(search_text) != -1:
                return True
            if counter == 9:
                print("Failed to get the inner text for our web element ( {0} )".format(xpath))
                return False