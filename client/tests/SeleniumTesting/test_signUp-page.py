

import unittest
from faker import Faker
from selenium import webdriver
import pages as page
from locators import PageLocators

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

        # Content page after the user sign ups
        self.content_page = page.ContentPage(self.driver)

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

    def test_verify_user_is_unable_to_sign_up_with_password_that_does_not_meet_the_password_complexity_requirements(self):
        """ Test 7. Testing with different password requirement and confirm if password is complexity works """

        self.signUp_page.pwd_element = "Testing@1"
        self.signUp_page.click_submit_button()

        # Assertions
        self.assertTrue("Testing@1")

    def test_Verify_that_the_user_is_able_to_successfully_sign_up_with_valid_details(self):
        """ Test 8. Test if user is able to sign up with valid details """

        email = self.fake.email()
        self.signUp_page.email_element = email
        self.signUp_page.pwd_element = self.fake.password()
        self.signUp_page.click_submit_button()

        # Assertions
        self.assertIsNotNone(self.content_page.profile_cirlce())
        self.assertEquals(self.content_page.get_email().text, email)

    def test_Verify_that_the_user_is_redirected_to_the_correct_page_after_successfully_signing_up(self):
        """ Test 9. Test if user is able to redirect to correct page after sign up """
        email = self.fake.email()
        self.signUp_page.email_element = email
        self.signUp_page.pwd_element = self.fake.password()
        self.signUp_page.click_submit_button()

        # Assertions
        self.assertIsNotNone(self.content_page.profile_cirlce())

    def test_verify_if_error_message_is_displayed_if_user_tries_to_sign_up_with_an_email_address_that_has_already_been_registered(self):
        """ Test 10. Test if error message is displayed if existing user tries to register again """

        # Sign Up Process
        email = self.fake.email() # 1234@gmail.com
        password = self.fake.password() # Abcde@99


        # Sign Up
        self.signUp_page.email_element = email
        self.signUp_page.pwd_element = password
        self.signUp_page.click_submit_button()
        # Logout
        # self.content_page.profile_cirlce().click()
        self.content_page.get_logout_button().click()
        # Signing up again with same credentials
        self.signUp_page.navigate_to_sign_up_page()
        self.signUp_page.email_element = email
        self.signUp_page.pwd_element = password
        self.signUp_page.click_submit_button()

        # Assertions
        self.assertIsNotNone(self.driver.find_element(*PageLocators.SIGNUP_ERR))
        self.assertEqual(self.driver.find_element(*PageLocators.SIGNUP_ERR).text,"Something went wrong, please try again later")

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
