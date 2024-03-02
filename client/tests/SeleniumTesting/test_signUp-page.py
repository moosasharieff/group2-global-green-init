

import time
import unittest
from faker import Faker
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NausiccaSignUpPage(unittest.TestCase):
    def setUp(self):
        """
        Setups testing enviroment for Automated Testing.
        :return: Opens selenium webdriver for Chrome
        """

        # Initating Chrome webdriver
        self.driver = webdriver.Chrome()
        self.driver.get("https://v1.globalgreeninit.world")
        self.wait = WebDriverWait(self.driver, 10)

        # Entering SignIn Section
        try:
            # Wait for 10 seconds or until the signUp element is available to click
            signInxpath = "//button[@class='mt-10 h-12 w-full rounded-lg bg-green-300 text-green-700 hover:bg-green-500 hover:text-white md:w-32']"
            signIn = self.wait.until(EC.element_to_be_clickable((By.XPATH, signInxpath)))

        except Exception:
            print(f"Unable to find {signInxpath}")
        finally:
            signIn.click()


        # Entering SignUp Section
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH,"//h1[@class='c3cef09c2 cbae2c229']")))
            self.wait.until(EC.element_to_be_clickable((By.ID, "username")))  # different for logIn page
            signUp = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='cc3100fd0 c316efbcd']")))
        except Exception as e:
            print(e)
        finally:
            # Enter into signUp page
            signUp.click()

        # Initiating variable for use in testing
        try:
            self.welcome = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@class='c3cef09c2 cbae2c229']")))
            self.email_Ck = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='input c2a857a25 c27e670b0']")))
            self.email_Txt = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='c2809db4e js-required c6bbe06f6 c5d75975c']")))
            self.password_Ck = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='input c2a857a25 c70ffb6a4']")))
            self.password_Txt = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='c2809db4e js-required c6bbe06f6 c005e1e8d']")))
            self.submit = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='action']")))
        except Exception as e:
            print(e)

        # Initiating faker to generate information
        self.fake = Faker()

    # @unittest.skip("Complete")
    def test_verify_if_signUp_loaded_correctly(self):
        textOnPage1 = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@class='cb1fa4186 c52248d64']")))
        textOnPage2 = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@class='cb1fa4186 c52248d64 c1f96d928']")))

        self.assertEqual(textOnPage1.text, "Sign Up to Nausicca's")
        self.assertEqual(textOnPage2.text, "Already have an account? Log in")

    # @unittest.skip("Complete")
    def test_verify_if_email_field_present_correctly(self):

        self.assertIsNotNone(self.email_Txt)
        self.assertIsNotNone(self.submit)
        self.assertEqual(self.email_Txt.text, "Email address")
        self.assertEqual(self.submit.text, "Continue")

    # @unittest.skip("Complete")
    def test_verify_if_password_field_present_correctly(self):

        self.assertIsNotNone(self.password_Txt)
        self.assertIsNotNone(self.submit)
        self.assertEqual(self.password_Txt.text, "Password")
        self.assertEqual(self.submit.text, "Continue")

    # @unittest.skip("Complete")
    def test_Verify_that_email_field_is_mandatory(self):

        # Checking if password field is left blank details
        self.email_Ck.click()
        self.email_Ck.send_keys(self.fake.email())
        self.submit.click()

        self.assertEqual(self.welcome.text, "Welcome")
        self.assertEqual(self.password_Txt.text, "Password")

    # @unittest.skip("Complete")
    def test_Verify_that_password_field_is_mandatory(self):

        # Checking if password field is left blank details
        self.email_Ck.clear()
        self.password_Ck.send_keys(self.fake.password())
        self.submit.click()

        self.assertEqual(self.welcome.text, "Welcome") # Upon entering submit with blank email, this field become blonk.
        pwd_error_msg = self.driver.find_element(By.XPATH, "//li[@class='c89df7c73 cd75ef6da']")
        self.assertIn(pwd_error_msg.text, "At least 8 characters")
        self.assertEqual(self.email_Txt.text, "Email address")

    def tearDown(self):
        """
        This program executes at the end of the test.
        """
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()