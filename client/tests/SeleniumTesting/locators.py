
from selenium.webdriver.common.by import By

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