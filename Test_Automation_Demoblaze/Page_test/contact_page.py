import time

import allure
from selenium.webdriver.common.by import By

from Bases.test_base import Base_test
from Locators import contact_locator


class Contact_page(Base_test):

    def __init__(self):
        self.contact=contact_locator.contact_link
        self.email=contact_locator.contact_email
        self.name=contact_locator.contact_name
        self.messages=contact_locator.contact_message
        self.close=contact_locator.close
        self.x_close=contact_locator.x_path
        self.message=contact_locator.send_message
        self.send = contact_locator.contact_send_message
        self.close = contact_locator.close_send_message
        self.x_button = contact_locator.x_button

    def common(self):
        super().base_for_web()
    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)

    def test_contact_us(self):
        self.common()
        self.driver.implicitly_wait(3)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.contact).click()
        self.driver.find_element(By.XPATH, self.email).send_keys("dessieelsa@gmail.com")
        self.driver.find_element(By.XPATH, self.name).send_keys("els")
        self.driver.find_element(By.XPATH, self.messages).send_keys("hello")
        self.driver.find_element(By.XPATH, self.message).click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()

    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_x(self):
        self.common()
        self.driver.implicitly_wait(3)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, self.contact).click()
        self.driver.find_element(By.XPATH, self.email).send_keys()
        self.driver.find_element(By.XPATH, self.name).send_keys("Dessie")
        self.driver.find_element(By.XPATH, self.message).send_keys()
        self.driver.find_element(By.XPATH, self.message).click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()

    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    def test_message_null(self):
        self.common()
        self.driver.implicitly_wait(3)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.contact).click()
        self.driver.find_element(By.XPATH, self.email).send_keys("Dessieelsa@gmail.com")
        self.driver.find_element(By.XPATH, self.name).send_keys("Dessie")
        self.driver.find_element(By.XPATH, self.message).send_keys()
        self.driver.find_element(By.XPATH, self.message).click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()

    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_email(self):
        self.common()
        self.driver.implicitly_wait(3)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.contact).click()
        self.driver.find_element(By.XPATH, self.email).send_keys()
        self.driver.find_element(By.XPATH, self.name).send_keys("Dessie")
        self.driver.find_element(By.XPATH, self.message).send_keys("asdfghjkllkjh")
        self.driver.find_element(By.XPATH, self.message).click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()

    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_page(self):
        self.common()
        self.driver.implicitly_wait(3)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.contact).click()
        self.driver.find_element(By.XPATH, self.email).send_keys("dessieelsa@gmail.com")
        self.driver.find_element(By.XPATH, self.name).send_keys("elsa")
        self.driver.find_element(By.XPATH, self.message).send_keys("Hellow world")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.send).click()

    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_page_email_null(self):
        self.common()
        self.driver.implicitly_wait(3)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.contact).click()
        self.driver.find_element(By.XPATH, self.email).send_keys("")
        self.driver.find_element(By.XPATH, self.name).send_keys("elsa")
        self.driver.find_element(By.XPATH, self.message).send_keys("Hellow world")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.send).click()

    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_page_username_null(self):
        self.common()
        self.driver.implicitly_wait(3)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.contact).click()
        self.driver.find_element(By.XPATH, self.email).send_keys("wubristasnakew@gmail.com")
        self.driver.find_element(By.XPATH, self.name).send_keys("")
        self.driver.find_element(By.XPATH, self.message).send_keys("Hellow world")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.send).click()

    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_page_message_null(self):
        self.common()
        self.driver.implicitly_wait(3)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.contact).click()
        self.driver.find_element(By.XPATH, self.email).send_keys("dessielsa@gmail.com")
        self.driver.find_element(By.XPATH, self.name).send_keys("elsa")
        self.driver.find_element(By.XPATH, self.message).send_keys()
        self.driver.find_element(By.XPATH, self.send).click()

    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_page_close_button(self):
        self.common()
        self.driver.implicitly_wait(3)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.contact).click()
        self.driver.find_element(By.XPATH, self.email).send_keys("elsadessie@gmail.com")
        self.driver.find_element(By.XPATH, self.name).send_keys("elsa")
        self.driver.find_element(By.XPATH, self.message).send_keys("Hellow world")
        self.driver.find_element(By.XPATH, self.close).click()
        time.sleep(3)

    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_page_NULL_username_Passward(self):
        self.common()
        self.driver.implicitly_wait(3)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.contact).click()
        self.driver.find_element(By.XPATH, self.email).send_keys("elsadessi@gmail.com")
        self.driver.find_element(By.XPATH, self.name).send_keys()
        self.driver.find_element(By.XPATH, self.message).send_keys("Hellow world")
        self.driver.find_element(By.XPATH, self.send).click()


    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_page_x_button(self):
        self.common()
        self.driver.implicitly_wait(3)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.contact).click()
        self.driver.find_element(By.XPATH, self.email).send_keys("elsdsefafaew@gmail.com")
        self.driver.find_element(By.XPATH, self.name).send_keys("elsa")
        self.driver.find_element(By.XPATH, self.message).send_keys("Hellow world")
        self.driver.find_element(By.XPATH, self.x_button).click()

    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_page_x_button_incorrect_page(self):
        self.common()
        self.driver.implicitly_wait(3)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.contact).click()
        self.driver.find_element(By.XPATH, self.email).send_keys("eesldfsrede@gmail.com")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.name).send_keys("elsa")
        self.driver.find_element(By.XPATH, self.message).send_keys("Hellow world")
        self.driver.find_element(By.XPATH, self.x_button).click()

    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_page_close_button_incorrect_page(self):
        self.common()
        self.driver.implicitly_wait(3)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.contact).click()
        self.driver.find_element(By.XPATH, self.email).send_keys()
        self.driver.find_element(By.XPATH, self.name).send_keys()
        self.driver.find_element(By.XPATH, self.message).send_keys("Hellow world")
        self.driver.find_element(By.XPATH, self.x_button).click()


    @allure.step
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_page_send_button_incorrect(self):
        self.common()
        self.driver.implicitly_wait(3)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.contact).click()
        self.driver.find_element(By.XPATH, self.email).send_keys()
        self.driver.find_element(By.XPATH, self.name).send_keys("")
        self.driver.find_element(By.XPATH, self.message).send_keys("Hellow world")
        self.driver.find_element(By.XPATH, self.send).click()
        self.driver.find_element(By.XPATH, self.x_button).click()







