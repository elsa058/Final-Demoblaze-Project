from selenium import webdriver


# from webdriver_manager.chrome import ChromeDriverManager
class Base_test():

    def base_for_web(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.maximize_window()
        return self.driver
    def close(self):
        self.driver.quit()
        self.driver.close()