import time


from selenium.webdriver.common.by import By

from Bases.test_base import Base_test
from Locators.Signup_locators import *
class Test_page(Base_test):

    def __init__(self):
        self.link=Test_Link.x_signin
        self.name=Test_Link.username
        self.password=Test_Link.userpass
        self.button=Test_Link.x_button_signup
        self.close=Test_Link.x_close_button


    def common(self):
        super().base_for_web()
    def test_signup(self):
        self.common()
        self.driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.link).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.name).send_keys("dina yohannes")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.password).send_keys("12345")
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.button).click()
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(2)

    def test_username(self):
        self.common()
        self.driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.link).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.name).send_keys("dina yohannes")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.password).send_keys()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.button).click()
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(2)

    def test_empty_fields(self):
        self.common()
        self.driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.link).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.name).send_keys()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.password).send_keys()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.button).click()
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(2)

    def test_close_button(self):
        self.common()
        self.driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.link).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.close).click()
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(3)

