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
        #email field
        self.driver.find_element(By.XPATH,"//*[@id=':r2:']").send_keys(constants.EMAIL)
        #proceed button
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div/div[1]/div[2]/form/button").click()
        time.sleep(2)
        #password field
        self.driver.find_element(By.XPATH,"//*[@id=':rn:']").send_keys(constants.PASS)
        #login button
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div/div[1]/div[2]/form/button").click()

    
