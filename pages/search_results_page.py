from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_result_text = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
        self.next_page_button = (By.CSS_SELECTOR, "a.s-pagination-item.s-pagination-next")

    def get_search_result_text(self):
        return self.wait_for_element(*self.search_result_text).text

    def go_to_next_page(self):
        self.click_element(*self.next_page_button)
