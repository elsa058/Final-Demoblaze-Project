import pytest
import allure
from Page_test.cart_page import Test_cart_page


class Test_page:
    @allure.description("Test Cart page")
    @pytest.mark.sanity
    def test_cart_page(self):
        test = Test_cart_page()
        test.cart_page()

    def test_cart(self):
        test = Test_cart_page()
        test.test_cart_page()

    def test_cart_page_invalid(self):
        test = Test_cart_page()
        test.test_cart_page_invalid()

    def test_cart_page_social_character(self):
        test = Test_cart_page()
        test.test_cart_page_social_character()

    def test_cart_page_social_character_Null(self):
        test = Test_cart_page()
        test.test_cart_page_social_character_Null()

    def test_cart_page_social_close(self):
        test = Test_cart_page()
        test.test_cart_page_social_close()

    def test_cart_page_social_X(self):
        test = Test_cart_page()
        test.test_cart_page_social_X()
