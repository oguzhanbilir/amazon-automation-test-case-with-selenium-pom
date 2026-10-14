from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.amazon.com.tr/gp/cart/view.html"
        self.product_title = (By.CSS_SELECTOR, ".sc-product-title")
        self.delete_button = (By.CSS_SELECTOR, "[data-feature-id='item-delete-button'] input, input[value='Sil']")
        self.cart_count = (By.ID, "nav-cart-count")
        self.logo = (By.ID, "nav-logo-sprites")

    def open(self):
        self.driver.get(self.url)

    def get_product_title(self):
        return self.wait_for_element(*self.product_title).text

    def delete_first_item(self):
        self.click_element(*self.delete_button)

    def wait_until_cart_count_is(self, expected, timeout=10):
        # Sayaç sayfa yenilenmeden güncellendiği için metnin değişmesini bekliyoruz.
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.cart_count, expected)
        )
        return self.driver.find_element(*self.cart_count).text

    def go_to_home_page(self):
        self.click_element(*self.logo)
