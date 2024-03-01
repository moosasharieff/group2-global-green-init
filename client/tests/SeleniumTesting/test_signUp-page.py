

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
            signUp = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='mt-10 h-12 w-full rounded-lg bg-green-300 text-green-700 hover:bg-green-500 hover:text-white md:w-32']")))
            signUp.click()
        except Exception as e:
            print(e)

    def tearDown(self):
        """
        This program executes at the end of the test.
        """
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()