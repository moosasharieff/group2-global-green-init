
from selenium.webdriver.common.by import By

class VARIABLES(object):
    URL = "https://v2.globalgreeninit.world/"

class HomePageLocators(object):
    SIGNIN = (By.XPATH, "//button[@type='submit']")  # Entering from homepage to signIn page

class SignUpPageLocators:
    WELCOME = (By.XPATH, "//h1")
    EMAIL_CLK = (By.XPATH, "//input[@id='email']") # Able to set value to Email
    EMAIL_TXT = (By.XPATH, "//div[@data-dynamic-label-for='email']")
    EMAIL_ERR = (By.ID, 'error-element-email')
    PASSWORD_CLK = (By.XPATH, "//input[@id='password']")
    PASSWORD_TXT = (By.XPATH, "//div[@data-dynamic-label-for='password']")
    PASSWORD_ERR = (By.XPATH, "//li[@data-error-code='password-policy-length-at-least']")
    PASSWORD_COMPLEXITY = (By.XPATH, "//div[@class='cf325142a']")
    SIGNUP = (By.XPATH, "//a[@class='ce78228eb cfe4c492b']")  # Entering from signIn page to singUp page (LOGIN)
    SIGNUP_ERR = (By.XPATH, "//div[@id='prompt-alert']")
    SUBMIT = (By.NAME, "action") # Entering from


class ContentPageLocators(object):
    CIRCLE_LINK = (By.XPATH, "//div[@class='h-12 w-12 cursor-pointer rounded-full bg-black']")
    LOGGED_EMAIL = (By.XPATH, "//div[@class='grid grid-rows-2']//p")
    LOGOUT_BUTTON = (By.XPATH, "//div[@class='grid grid-rows-2']//button")

class SignInPageLocators:
    SIGNIN = (By.XPATH, "//button[@type='submit']")
    EMAIL_CLK = (By.ID, "username")  # Able to set value to Email
    EMAIL_TXT = (By.XPATH, "//div[@data-dynamic-label-for='username']")
    PASSWORD_CLK = (By.ID, "password")
    PASSWORD_TXT = (By.XPATH, "//div[@data-dynamic-label-for='password']")
    FORGOT_PASSWORD = (By.XPATH, "//a[@class='ce78228eb c80853310 cfe4c492b']")
    EMAIL_FORGOT_PASSWORD = (By.ID, "email") # Email box on forgot password page
    FORGOT_PASSWORD_PAGE = (By.XPATH, "//h1[@class='c75a821d8 cf4ccfc47']") # Forgot Password Text on forgot password page
    USER_EMAIL = "moosasharieff@gmail.com"
    USER_PASSWORD = "testing@123"
    INCORRECT_EMAIL_OR_PASSWORD = (By.XPATH, "//span[@id='error-element-password']")
    CARDS = (By.XPATH, "//img[@class='rounded-xl object-fill']")
    BACK_TO_LOGIN = (By.XPATH, "//button[@value='back-to-login']")
    EMAIL_CONFIRMATION = (By.XPATH, "//h1[@role='presentation']")