import pytest
from pytest import mark
import allure
from Page_test.home_page import *


class Test_Home:
    @allure.description("Test HomePage phone catagories")
    @pytest.mark.sanity
    def test_iphon_6(self):
        test = Home_page()
        test.test_iphone_6()

    @allure.description("Test HomePage phone catagories")
    @pytest.mark.sanity
    def test_samsung_s6(self):
        test = Home_page()
        test.test_samsung_s6()

    @allure.description("Test HomePage phone catagories")
    @pytest.mark.sanity
    def test_assus_full_HD(self):
        test = Home_page()
        test.test_assus()

    @allure.description("Test HomePage phone catagories")
    @pytest.mark.sanity
    def test_Apple_Monitor(self):
        test = Home_page()
        test.test_apple_monitor()

    @allure.description("Test HomePage phone catagories")
    @pytest.mark.sanity
    def test_Nokia_Lumi(self):
        test = Home_page()
        test.Test_Nokia_Lumui()

    @allure.description("Test HomePage phone catagories")
    @pytest.mark.sanity
    def test_curser(self):
        test = Home_page()
        test.test_curser()
