from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # Локаторы
    TITLE = (By.CLASS_NAME, "title")
    PRODUCTS_CONTAINER = (By.ID, "inventory_container")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    
    def is_displayed(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.PRODUCTS_CONTAINER))
            return True
        except:
            return False
    
    def get_title(self):
        return self.driver.find_element(*self.TITLE).text
    
    def get_current_url(self):
        return self.driver.current_url