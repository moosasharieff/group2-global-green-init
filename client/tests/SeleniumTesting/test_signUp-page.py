

import time
import unittest
from selenium import webdriver
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

        try:
            # Wait for 10 seconds or until the signUp element is available to click
            signInxpath = "//button[@class='mt-10 h-12 w-full rounded-lg bg-green-300 text-green-700 hover:bg-green-500 hover:text-white md:w-32']"
            signIn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, signInxpath)))
            signIn.click()
        except Exception:
            print(f"Unable to find {signInxpath}")

        try:
            self.welcome = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//h1[@class='c3cef09c2 cbae2c229']")))
            self.username = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "username")))  # different for logIn page
            # self.email = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "email"))) # different for logIn page
            self.password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))
            # self.Fpassword = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='cc3100fd0 cbd40558e c316efbd']")))
            self.signUp = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='cc3100fd0 c316efbcd']")))
            self.submit = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "action")))
        except Exception as e:
            print(e)

        # Enter into signUp page
        self.signUp.click()

    # @unittest.skip("Write test cases later")
    def test_verify_if_signUp_loaded_correctly(self):
        textOnPage1 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[@class='cb1fa4186 c52248d64']")))
        textOnPage2 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[@class='cb1fa4186 c52248d64 c1f96d928']")))

        self.assertEqual(textOnPage1.text, "Sign Up to Nausicca's")
        self.assertEqual(textOnPage2.text, "Already have an account? Log in")

    def test_verify_if_email_field_present_correctly(self):
        try:
            email = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='c2809db4e js-required c6bbe06f6 c5d75975c']")))
            submit = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@name='action']")))
        except Exception as e:
            print(e)

        self.assertIsNotNone(email)
        self.assertIsNotNone(submit)
        self.assertEqual(email.text, "Email address")
        self.assertEqual(submit.text, "Continue")

    def test_verify_if_password_field_present_correctly(self):
        try:
            password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='c2809db4e js-required c6bbe06f6 c005e1e8d']")))
            submit = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@name='action']")))
        except Exception as e:
            print(e)

        self.assertIsNotNone(password)
        self.assertIsNotNone(submit)
        self.assertEqual(password.text, "Password")
        self.assertEqual(submit.text, "Continue")

    def tearDown(self):
        """
        This program executes at the end of the test.
        """
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()