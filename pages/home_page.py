from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.amazon.com.tr/"
        self.search_box = (By.ID, "twotabsearchtextbox")
        self.cookies_accept_button = (By.ID, "sp-cc-accept")

    def open(self):
        self.driver.get(self.url)

    def accept_cookies(self):
        self.click_element(*self.cookies_accept_button)

    def search_for(self, text):
        self.enter_text(*self.search_box, text)
        self.driver.find_element(*self.search_box).send_keys(Keys.ENTER)