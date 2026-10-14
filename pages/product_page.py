from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_title = (By.ID, "productTitle")
        self.add_to_cart_button = (By.ID, "add-to-cart-button")
        self.see_all_buying_options = (By.ID, "buybox-see-all-buying-choices")
        self.offer_add_to_cart_button = (By.CSS_SELECTOR, "input[name='submit.addToCart']")
        self.cart_count = (By.ID, "nav-cart-count")

    def get_product_title(self):
        return self.wait_for_element(*self.product_title).text

    def is_purchasable(self):
        # Stokta olmayan ya da sadece bilgi sayfası olan ürünlerde iki buton da bulunmaz.
        return (self.is_displayed(*self.add_to_cart_button)
                or self.is_displayed(*self.see_all_buying_options))

    def add_to_cart(self):
        # Ürünün kendi "Sepete Ekle" butonu yoksa tüm satın alma seçeneklerinden ilk teklifi sepete ekliyoruz.
        try:
            self.click_element(*self.add_to_cart_button, timeout=5)
        except TimeoutException:
            self.click_element(*self.see_all_buying_options)
            self.click_element(*self.offer_add_to_cart_button)

    def get_cart_count(self):
        return self.wait_for_element(*self.cart_count).text
