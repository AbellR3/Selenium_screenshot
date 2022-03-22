from hashlib import new
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class BaseClass:
    def __init__(self, url, webdriver_path) -> None:
        self.driver = webdriver.Chrome(webdriver_path)
        self.base_url = url
        
    def find_element(self, locator:str, time:int=10) -> object:
        return WebDriverWait (self.driver, time).until(EC.presence_of_element_located(locator), message = "can't find element")

    def find_elements(self, locator:str, time:int=10) -> object:
        return WebDriverWait (self.driver, time).until(EC.presence_of_all_elements_located(locator), message = "can't find elements")

    def go_to_site(self):
        return self.driver.get(self.base_url)






