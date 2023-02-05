import time

from selenium.webdriver.common.by import By

from Test_Automation_Demoblaze.Bases.test_base import Base_test
from Locators.about_us_locators import about_page


class About_us(Base_test):

    def __init__(self):
        self.about=about_page.link_about
        self.exist=about_page.about_x
        self.video=about_page.video
        self.button = about_page .link_about
        self.link = about_page.about_x
        self.close = about_page.about_close

    def common(self):
        super().base_for_web()

    def test_about_us(self):
        self.common()
        self.driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.about).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.video).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.exist).click()
        time.sleep(3)

    def test_about_us_page(self):
        self.common()
        self.driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.button).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.link).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.close).click()
        time.sleep(3)




