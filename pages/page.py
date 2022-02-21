from unicodedata import name
from selenium.webdriver.common.by import By

class BasePage:
        def __init__(self, browser, wait):
            self.browser = browser
            self.wait = wait
            
class LoginPage(basePage):
    user_name_locator = (By.ID, "user-name")            
    password = (By.ID, "password")
    login_button_locator = (By.ID,"login-button")
    error_box = (By.CSS_SELECTOR, ".error-message-container")

    def login(self, user_name, password):
        user_name_input = self.browser.find_element(*self.user_name)        
        user_name_input.send_keys(user_name)    
            
            
class ProductsPage(Base page)            
            
            
            
            
            pass