import allure
import pytest

from Page_test.Signup_page import *


class Test_link():
    @allure.description("Test valid signup")
    # @pytest.Mark.sanity
    def test_signup(self):
        test = Test_page()
        test.test_signup()
    def test_username(self):
        test=Test_page()
        test.test_username()

    def test_empty_fields(self):
        test = Test_page()
        test.test_empty_fields()

    def test_close_button(self):
        test = Test_page()
        test.test_close_button()
