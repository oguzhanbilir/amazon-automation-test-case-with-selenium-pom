from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_title = (By.ID, "productTitle")
        self.add_to_cart_button = (By.ID, "add-to-cart-button")
        self.cart_count = (By.ID, "nav-cart-count")

    def get_product_title(self):
        return self.wait_for_element(*self.product_title).text

    def add_to_cart(self):
        self.click_element(*self.add_to_cart_button)

    def get_cart_count(self):
        return self.wait_for_element(*self.cart_count).text