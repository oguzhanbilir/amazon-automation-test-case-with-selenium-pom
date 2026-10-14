from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        # Çerez bandı her ziyarette çıkmayabilir; çıkmadıysa devam ediyoruz.
        try:
            self.click_element(*self.cookies_accept_button, timeout=5)
        except TimeoutException:
            pass

    def search_for(self, text):
        self.enter_text(*self.search_box, text)
        self.driver.find_element(*self.search_box).send_keys(Keys.ENTER)
