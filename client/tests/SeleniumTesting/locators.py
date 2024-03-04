
from selenium.webdriver.common.by import By

class HomePageLocators(object):
    SIGNIN = (By.XPATH, "//button[@type='submit']")  # Entering from homepage to signIn page

class SignUpPageLocators:
    WELCOME = (By.XPATH, "//h1[@class='c3cef09c2 cbae2c229']")
    EMAIL_CLK = (By.XPATH, "//input[@class='input c2a857a25 c27e670b0']") # Able to set value to Email
    EMAIL_TXT = (By.XPATH, "//div[@class='c2809db4e js-required c6bbe06f6 c5d75975c']")
    EMAIL_ERR = (By.ID, 'error-element-email')
    PASSWORD_CLK = (By.XPATH, "//input[@class='input c2a857a25 c70ffb6a4']")
    PASSWORD_TXT = (By.XPATH, "//div[@class='c2809db4e js-required c6bbe06f6 c005e1e8d']")
    PASSWORD_ERR = (By.XPATH, "//li[@data-error-code='password-policy-length-at-least']")
    PASSWORD_COMPLEXITY = (By.XPATH, "//div[@class='cf325142a']")
    SIGNUP = (By.XPATH, "//a[@class='cc3100fd0 c316efbcd']")  # Entering from signIn page to singUp page (LOGIN)
    SIGNUP_ERR = (By.XPATH, "//p[@class='ce3cf3592 c409e6d91']")
    SUBMIT = (By.NAME, "action") # Entering from


class ContentPageLocators(object):
    CIRCLE_LINK = (By.XPATH, "//div[@class='h-12 w-12 cursor-pointer rounded-full bg-black']")
    LOGGED_EMAIL = (By.XPATH, "//div[@class='grid grid-rows-2']//p")
    LOGOUT_BUTTON = (By.XPATH, "//div[@class='grid grid-rows-2']//button")