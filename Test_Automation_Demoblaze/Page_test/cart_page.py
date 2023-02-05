import time

import allure
from selenium.webdriver.common.by import By
from Bases.test_base import Base_test
from Locators.Cart_Locators import Cart_Page_Locators


class Test_cart_page(Base_test):

    def __init__(self):
        self.button=Cart_Page_Locators.cart_button
        self.order= Cart_Page_Locators.click_place_order_button
        self.name = Cart_Page_Locators.total_name
        self.country = Cart_Page_Locators.country_name
        self.city = Cart_Page_Locators.city_name
        self.card = Cart_Page_Locators. cridit_carde
        self.month = Cart_Page_Locators.month
        self.year = Cart_Page_Locators.year
        self.purchase = Cart_Page_Locators.purchase
        self.close = Cart_Page_Locators.close_button
        self.button = Cart_Page_Locators.cart_button
        self.order = Cart_Page_Locators.click_place_order_button
        self.Xpath_name = Cart_Page_Locators.path_name
        self.Name = Cart_Page_Locators.name
        self.card = Cart_Page_Locators.cridit_carde
        self.Card_no = Cart_Page_Locators.Card
        self.MONTH = Cart_Page_Locators.mo_nth
        self.YEAR = Cart_Page_Locators.ye_ar
        self.purchase = Cart_Page_Locators.purchase
        self.close = Cart_Page_Locators.close_button
        self.Null = Cart_Page_Locators.null
        self.special_character = Cart_Page_Locators.special_character
        self.X = Cart_Page_Locators.x


    def common(self):
        super().base_for_web()

    def cart_page(self):
        self.common()
        self.driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.button).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.order).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.name).send_keys("elsa")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.country).send_keys("israel")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.city).send_keys("Be'ersheva")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.card).send_keys("3456789765456787")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.month).send_keys("may")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.year).send_keys("8/30/2023")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.purchase).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.close).click()
        time.sleep(3)

    @allure.description("cart valid placeholder address")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_page(self):
        self.common()
        self.driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.button).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.order).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Xpath_name).send_keys(self.Name)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.country).send_keys(self.country)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.city).send_keys(self.city)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.card).send_keys(self.Card_no)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.month).send_keys(self.MONTH)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.year).send_keys(self.YEAR)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.purchase).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.close).click()
        time.sleep(3)

    @allure.description("cart invalid placeholder address")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_page_invalid(self):
        self.common()
        self.driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.button).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.order).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Xpath_name).send_keys(self.Null)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.country).send_keys(self.Null)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.city).send_keys(self.Null)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.card).send_keys(self.Null)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.month).send_keys(self.Null)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.year).send_keys(self.Null)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.purchase).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.close).click()
        time.sleep(3)

    @allure.description("cart invalid placeholder address")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_page_social_character(self):
        self.common()
        self.driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.button).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.order).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Xpath_name).send_keys(self.special_character)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.country).send_keys(self.country)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.city).send_keys(self.city)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.card).send_keys(self.special_character)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.month).send_keys(self.Null)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.year).send_keys(self.YEAR)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.purchase).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.close).click()
        time.sleep(3)

    @allure.description("cart invalid placeholder address")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_page_social_character_Null(self):
        self.common()
        self.driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.button).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.order).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Xpath_name).send_keys(self.Name)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.country).send_keys(self.country)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.city).send_keys(self.city)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.card).send_keys(self.special_character)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.month).send_keys(self.Null)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.year).send_keys(self.Null)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.purchase).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.close).click()
        time.sleep(3)

    @allure.description("cart invalid placeholder address")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_page_social_close(self):
        self.common()
        self.driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.button).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.order).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Xpath_name).send_keys(self.Name)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.country).send_keys(self.country)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.city).send_keys(self.city)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.card).send_keys(self.special_character)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.month).send_keys(self.Null)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.year).send_keys(self.Null)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.close).click()
        time.sleep(3)

    @allure.description("cart invalid placeholder address")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_page_social_X(self):
        self.common()
        self.driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.button).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.order).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Xpath_name).send_keys(self.Name)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.country).send_keys(self.country)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.city).send_keys(self.city)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.card).send_keys(self.special_character)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.month).send_keys(self.Null)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.year).send_keys(self.Null)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.X).click()
        time.sleep(3)


