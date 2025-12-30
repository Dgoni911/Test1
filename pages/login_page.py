from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        return self
    
    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        return self
    
    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        return self
    
    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)
    
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        return self.click_login()
    
    def get_error_message(self):
        try:
            return self.driver.find_element(*self.ERROR_MESSAGE).text
        except:
            return None