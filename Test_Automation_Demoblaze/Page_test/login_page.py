import time

import allure
from selenium.webdriver.common.by import By

from Bases.test_base import Base_test
from Locators.login_locators import *
class Test_login(Base_test):

    def __init__(self):
        self.logging = Test_login.login
        self.user = Test_login.loguser
        self.password = Test_login.logpass
        self.button = Test_login.logbutton
        self.login_button =Test_login .login_button
        self.name = Test_login.correct_user_name
        self.passward = Test_login.correct_passward
        self.login = Test_login.login
        self.close = Test_login.close_button
        self.x_button = Test_login.x_path_button

    def common(self):
        super().base_for_web()

    def test_login(self):
        self.common()
        self.driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.logging).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.user).send_keys("elsa")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.password).send_keys("12345")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.button).click()
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(2)


    @allure.step
    @allure.description("test_login_username_passward_correct_page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_passward_correct_page(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.login_button).click()

        self.driver.find_element(By.XPATH, self.name).send_keys("elsa")

        self.driver.find_element(By.XPATH, self.passward).send_keys("Wub123456")

        self.driver.find_element(By.XPATH, self.login).click()

        # self.driver.find_element(By.XPATH, self.close).click()

    @allure.step
    @allure.description("test_login_username_passward_correct_Close_button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_passward_correct_Close_button(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.login_button).click()

        self.driver.find_element(By.XPATH, self.name).send_keys("elsa")

        self.driver.find_element(By.XPATH, self.passward).send_keys("Wub123456")

        # self.driver.find_element(By.XPATH, self.login).click()

        self.driver.find_element(By.XPATH, self.close).click()

    @allure.step
    @allure.description("test_login_username_NULL_passward_correct_page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_NULL_passward_correct_page(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.login_button).click()

        self.driver.find_element(By.XPATH, self.name).send_keys("elsa")

        self.driver.find_element(By.XPATH, self.passward).send_keys("els123456")

        self.driver.find_element(By.XPATH, self.login).click()

        # self.driver.find_element(By.XPATH, self.close).click()

    @allure.step
    @allure.description("test_login_correct_username_passward_NULL")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_correct_username_passward_NULL(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.login_button).click()

        self.driver.find_element(By.XPATH, self.name).send_keys("elsa")

        self.driver.find_element(By.XPATH, self.passward).send_keys("els123456")

        self.driver.find_element(By.XPATH, self.login).click()

        # self.driver.find_element(By.XPATH, self.close).click()

    @allure.step
    @allure.description("test_login_username_passward_correct_page_x_button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_passward_correct_page_x_button(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.login_button).click()

        self.driver.find_element(By.XPATH, self.name).send_keys("elsa")

        self.driver.find_element(By.XPATH, self.passward).send_keys("els123456")

        self.driver.find_element(By.XPATH, self.x_button).click()

        # self.driver.find_element(By.XPATH, self.close).click()

    @allure.step
    @allure.description("test_login_username_Page_NULL")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_Page_NULL(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.login_button).click()

        self.driver.find_element(By.XPATH, self.name).send_keys()

        self.driver.find_element(By.XPATH, self.passward).send_keys("Wub123456")

        self.driver.find_element(By.XPATH, self.login).click()

        # self.driver.find_element(By.XPATH, self.close).click()

    @allure.step
    @allure.description("test_login_passward_page_NULL")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_passward_page_NULL(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.login_button).click()

        self.driver.find_element(By.XPATH, self.name).send_keys("elsa")

        self.driver.find_element(By.XPATH, self.passward).send_keys()

        self.driver.find_element(By.XPATH, self.login).click()

        # self.driver.find_element(By.XPATH, self.close).click()

    @allure.step
    @allure.description("test_login_username_passward_page_NULL")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_passward_page_NULL(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.login_button).click()

        self.driver.find_element(By.XPATH, self.name).send_keys()

        self.driver.find_element(By.XPATH, self.passward).send_keys()

        self.driver.find_element(By.XPATH, self.login).click()

        # self.driver.find_element(By.XPATH, self.close).click()

    @allure.step
    @allure.description("test_login_username_passward_page_incorrect")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_passward_page_incorrect(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.login_button).click()

        self.driver.find_element(By.XPATH, self.name).send_keys()

        self.driver.find_element(By.XPATH, self.passward).send_keys()

        self.driver.find_element(By.XPATH, self.login).click()

        self.driver.find_element(By.XPATH, self.close).click()

    @allure.step
    @allure.description("test_login_username_correct_passward_page_incorrect")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_correct_passward_page_incorrect(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.login_button).click()

        self.driver.find_element(By.XPATH, self.name).send_keys()

        self.driver.find_element(By.XPATH, self.passward).send_keys()

        self.driver.find_element(By.XPATH, self.login).click()

        self.driver.find_element(By.XPATH, self.close).click()