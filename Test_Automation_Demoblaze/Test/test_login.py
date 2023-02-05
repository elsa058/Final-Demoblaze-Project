
import pytest

from Page_test.login_page import *


class Test():
    @allure.description("Test valid login")
    # @pytest.Mark.sanity
    def test_login(self):
        test = Test_login()
        test.test_login()
    @allure.description("test_login_username_passward_correct_page")
    @pytest.mark.sanity
    def test_Login_page(self):
        test =Test_login()
        test.test_login_username_passward_correct_page()

    @allure.description("test_login_username_passward_correct_Close_button")
    @pytest.mark.sanity
    def test_login_close__page(self):
        test =Test_login()
        test.test_login_username_passward_correct_Close_button()

    @allure.description("test_login_username_NULL_passward_correct_page")
    @pytest.mark.sanity
    def test_login_username_NULL_passward_correct_page(self):
        test = Test_login ()
        test.test_login_username_NULL_passward_correct_page()

    @allure.description("test_login_correct_username_passward_NULL")
    @pytest.mark.sanity
    def test_login_correct_username_passward_NULL(self):
        test = Test_login()
        test.test_login_correct_username_passward_NULL()

    @allure.description("test_iphone_6")
    @pytest.mark.sanity
    def test_login_username_passward_correct_page_x_button(self):
        test = Test_login()
        test.test_login_username_passward_correct_page_x_button()

    @allure.description("test_login_username_Page_NULL")
    @pytest.mark.sanity
    def test_login_username_Page_NULL(self):
        test =Test_login()
        test.test_login_username_Page_NULL()

    @allure.description("test_login_passward_page_NULL")
    @pytest.mark.sanity
    def test_login_passward_page_NULL(self):
        test = Test_login ()
        test.test_login_passward_page_NULL()

    # @allure.description("test_login_username_passward_page")
    # @pytest.mark.sanity
    # def test_login_username_passward_page_NULL(self):
    #     test = Test_login ()
    #     test.test_login_username_passward_page()
    #
    # @allure.description("test_login_username_passward_page")
    # @pytest.mark.sanity
    # def test_login_username_passward_page_incorrect(self):
    #     test = Test_login ()
    #     test.test_login_username_passward_page()
    #
    # @allure.description("test_login_username_passward_page")
    # @pytest.mark.sanity
    # def test_login_username_correct_passward_page_incorrect(self):
    #     test = Test_login ()
    #     test.test_login_username_passward_page()