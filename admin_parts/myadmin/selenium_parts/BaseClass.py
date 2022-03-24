from hashlib import new
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import typing

class BaseClass:
    def __init__(self, url:str, driver_path:str ='./chromedriver') -> None:
        self.url:str = url
        self.driver = webdriver.Chrome(driver_path)
        self.driver.maximize_window()
        
    def find_element(self, locator:tuple, time:int=15) -> object:
        return WebDriverWait (self.driver, time).until(EC.presence_of_element_located(locator), message = "can't find element")

    def find_elements(self, locator:str, time:int=15) -> object:
        return WebDriverWait (self.driver, time).until(EC.presence_of_all_elements_located(locator), message = "can't find elements")

    def go_to_site(self):
        return self.driver.get(self.url)




class ElementFinder(BaseClass):

    def __init__(self,url:str, selector_type:str, driver_path:str ='./chromedriver') -> None:
        super().__init__(url, driver_path)

        if selector_type == 'id':
            self.selector_type = By.ID
        elif selector_type == 'XPATH':
            self.selector_type =By.XPATH
        elif selector_type == 'class name':
            self.selector_type = By.CLASS_NAME
        else:
            self.selector_type = By.TAG_NAME


