import allure
import pytest

from Page_test.about_us_page import About_us

class Test_about_us():
    @allure.description("Test About us page")
    @pytest.mark.sanity
    def test_about_us(self):
        test =About_us ()
        test.test_about_us()

    def test_About_us_page(self):
        test = About_us()
        test.test_about_us_page()


