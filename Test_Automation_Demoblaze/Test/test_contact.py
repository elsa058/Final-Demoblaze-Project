import pytest

from Page_test.contact_page import *


class Test_contact:
    @allure.description("Test contact us page")
    @pytest.mark.sanity
    def test_contact_us(self):
        test = Contact_page()
        test.test_contact_us()

    @allure.description("Test contact us page")
    @pytest.mark.sanity
    def test_contact_x(self):
        test=Contact_page()
        test.test_contact_x()

    @allure.description("Test contact us page")
    @pytest.mark.sanity
    def test_message_null(self):
        test=Contact_page()
        test.test_message_null()

    @allure.description("Test contact us page")
    @pytest.mark.sanity
    def test_contact_email(self):
        test=Contact_page()
        test.test_contact_email()

    @allure.description("Test contact us page")
    @pytest.mark.sanity
    def test_contact_page_message_Null(self):
        test = Contact_page()
        test.test_contact_page_message_null()

    @allure.description("Test contact us page")
    @pytest.mark.sanity

    def test_contact_page_close_button(self):
        test =Contact_page()
        test.test_contact_page_close_button()

    @allure.description("Test contact us page")
    @pytest.mark.sanity

    def test_contact_page_x_button(self):
        test =Contact_page()
        test.test_contact_page_x_button()






