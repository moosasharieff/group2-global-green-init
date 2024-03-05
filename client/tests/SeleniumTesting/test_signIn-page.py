import time
import unittest
from faker import Faker
from selenium import webdriver
import pages as page
from locators import SignUpPageLocators

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