

import unittest
from faker import Faker
from selenium import webdriver
import pages as page

class Nausicca_Home_Page(unittest.TestCase):
    """ Test cases will be written here """

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://v2.globalgreeninit.world")

    def test_verify_if_home_page_is_opening(self):
        main_page = page.HomePage(self.driver)

        self.assertTrue(main_page.is_title_matches())
        self.assertEqual(main_page.click_signIn_button().text, "Sign Up")

    def tearDown(self) -> None:
        self.driver.quit()


class Nausicca_SignUp_Page(unittest.TestCase):
    """ Test cases will be written here """

    def setUp(self) -> None:
        # Navigate to SignUp page
        self.driver = webdriver.Chrome()
        self.driver.get("https://v2.globalgreeninit.world")

        # Navigate to SignUp page
        self.signUp_page = page.SignUpPage(self.driver)
        self.signUp_page.navigate_to_sign_up_page()

        # To generate fake data
        self.fake = Faker()

    def test_verify_if_email_field_present_correctly(self):
        """ Test 1. The email field is present """

        value = self.signUp_page.email_element.text
        welcomeTxt = self.signUp_page.welcome_element().text

        self.assertEqual(value, "Email address")
        self.assertEqual(welcomeTxt, "Welcome")

    def test_verify_if_password_field_present_correctly(self):
        """" Test 2. The Password field is preset """
        welcomeTxt = self.signUp_page.welcome_element().text
        value = self.signUp_page.pwd_element

        self.assertEqual(welcomeTxt, "Welcome")
        self.assertEqual(value, "Password")

    def test_Verify_that_email_field_is_mandatory(self):
        """ Test 3. The email field is mandatory and verify we are still on Sign Up after clicking on Sign Up button """

        self.signUp_page.pwd_element = self.fake.password(10)
        self.signUp_page.click_submit_button()

        # Assertions
        self.assertEqual(self.signUp_page.welcome_element().text, "Welcome")
        self.assertEqual(self.signUp_page.email_element.text, "Email address")
        self.assertEqual(self.signUp_page.pwd_element, "Password")

    def test_Verify_that_password_field_is_mandatory(self):
        """ Test 4. The Password field is mandatory and verify we are still on Sign Up after clicking on Sign Up button """

        self.signUp_page.email_element = self.fake.email()
        self.signUp_page.click_submit_button()

        # Assertions
        self.assertIn(self.signUp_page.get_passwordError().text, "At least 8 characters")


    def test_Verify_that_the_user_is_unable_to_sign_up_with_an_invalid_email_address(self):
        """ Test 5. Test if we are getting an error if we enter an invalid email address """
        emailVar = self.fake.email()
        emailVar = emailVar.split("@")[0]

        # Entering incompatible email credentials
        self.signUp_page.email_element = emailVar
        self.signUp_page.pwd_element = self.fake.password(10)
        self.signUp_page.click_submit_button()

        emailError = self.signUp_page.get_emailError().text

        # Assertions
        self.assertEqual(emailError, "Email is not valid.")

    def test_Verify_the_user_is_unable_to_sign_up_with_a_password_that_is_less_than_the_minimum_required_length(
            self):
        """ Test 6. Test if we are getting an error if we enter an invalid length of password """

        WrgPwd = self.fake.password()[:4]

        # Entering incompatible email credentials
        self.signUp_page.email_element = self.fake.email()
        self.signUp_page.pwd_element = WrgPwd
        self.signUp_page.click_submit_button()

        pwd_error_msg = self.signUp_page.get_passwordError().text

        # Assertions
        self.assertIn(pwd_error_msg, "At least 8 characters")

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
