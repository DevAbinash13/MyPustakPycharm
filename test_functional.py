from conftest import test_setup
import pytest
import constants
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("test_setup")
class Test_functional_tests():
    
    def test_open_website(self):
        self.driver.get(constants.URL)

    def test_login(self):
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div[1]/div/div[3]/div/div/button").click()   
        self.driver.find_element(By.XPATH,"//*[@id=':r2:']").send_keys("abinashlucky45@gmail.com")
