
from selenium.webdriver.common.by import By

class PageLocators(object):
    WELCOME = (By.XPATH, "//h1[@class='c3cef09c2 cbae2c229']")
    EMAIL_CLK = (By.XPATH, "//input[@class='input c2a857a25 c27e670b0']") # Able to set value to Email
    EMAIL_TXT = (By.XPATH, "//div[@class='c2809db4e js-required c6bbe06f6 c5d75975c']")
    PASSWORD_CLK = (By.XPATH, "//input[@class='input c2a857a25 c70ffb6a4']")
    PASSWORD_TXT = (By.XPATH, "//div[@class='c2809db4e js-required c6bbe06f6 c005e1e8d']")
    PASSWORD_ERR = (By.XPATH, "//li[@class='c89df7c73 cd75ef6da']")
    SUBMIT = (By.NAME, "action") # Entering from
    SIGNIN = (By.XPATH, "//button[@type='submit']") # Entering from homepage to signIn page
    SIGNUP = (By.XPATH, "//a[@class='cc3100fd0 c316efbcd']") # Entering from signIn page to singUp page

