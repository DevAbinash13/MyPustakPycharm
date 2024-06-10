from conftest import test_setup
import pytest
import constants
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

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

    def test_sum_displayed(self):
        BOOK_LIST = ["Crack Imu-Cet Entrance Exam","20 Practice Sets For Ibps Bank Clerk Preliminary Exam","Autobiography Of A Yogi"]
        sum= 0
        for i in BOOK_LIST:
            time.sleep(4)
            search_box = self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div[1]/div/div[2]/div/div/div/div/form/input")
            search_box.clear()
            search_box.clear()
            time.sleep(2)
            search_box.send_keys(i)
            self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div[1]/div/div[2]/div/div/div/div/form/button").click()
            time.sleep(2)
            book_element = self.driver.find_element(By.CLASS_NAME, "jsx-313054587")
            book_element.click()
            time.sleep(4)
            price_element = self.driver.find_element(By.XPATH, "//*[contains(@class, 'price')]")
            if "Free" in (price_element.text):
                sum = sum + 0
            else:
                split = ((price_element.text).split(" "))[0][1:]
                sum = sum + int(split)
            button = self.driver.find_element(By.XPATH, '//button[@type="button" and @value="Add to Cart"]')
            if button.text == "Add To Cart":
                button.click()
        cart = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div[1]/div/div[3]/div/span[2]")
        cart.click()



    
