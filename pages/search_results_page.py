from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_result_text = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
        self.next_page_button = (By.CSS_SELECTOR, "a.s-pagination-item.s-pagination-next")
        self.product_links = (By.CSS_SELECTOR, "div[data-component-type='s-search-result'] a:has(h2), div[data-component-type='s-search-result'] h2 a")

    def get_search_result_text(self):
        return self.wait_for_element(*self.search_result_text).text

    def go_to_next_page(self):
        self.click_element(*self.next_page_button)

    def select_product(self, position):
        # Sayfadaki arama sonuçlarından istenen sıradakini (1'den başlayarak) açıyoruz.
        self.wait_for_element(*self.product_links)
        products = self.driver.find_elements(*self.product_links)
        products[position - 1].click()
