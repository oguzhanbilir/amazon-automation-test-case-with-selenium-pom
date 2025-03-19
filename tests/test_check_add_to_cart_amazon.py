import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage

class TestCheckAddToCartAmazon(unittest.TestCase):
    def setUp(self):
        #test başlamadan önce gerekli ayarlamaları yapıyoruz.
        chromeOptions = Options()
        chromeOptions.add_argument('--disable-notifications')

        #chrome tarayıcısını başlatıyoruz ve pencereyi tam ekran yapıyoruz.
        self.driver = webdriver.Chrome(options=chromeOptions)
        self.driver.maximize_window()

        #tarayıcının elementleri bulmak için bekleyeceği süreyi ayarlıyoruz.
        self.driver.implicitly_wait(10)

        #sayfa class'ını başlatıyoruz.
        self.home_page = HomePage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.product_page = ProductPage(self.driver)

    def test_check_add_to_cart_amazon(self):
        #amazon.com.tr ana sayfasını açıyoruz.
        self.home_page.open()

        #çerezleri kabul ediyoruz.
        self.home_page.accept_cookies()

        #arama kutusuna 'Samsung' yazarak arama yapıyoruz.
        self.home_page.search_for("samsung")

        #arama sonuçlarını kontrol ediyoruz.
        search_result_text = self.search_results_page.get_search_result_text()
        self.assertIn("samsung", search_result_text.lower())

        #arama sonuçlarında 2. sayfaya geçiyoruz.
        self.search_results_page.go_to_next_page()
        self.assertIn("page=2", self.driver.current_url)

        #arama sonuçlarında 2. sayfada üçüncü ürünü (9. element) seçiyoruz.
        third_product = self.driver.find_element(By.CSS_SELECTOR, '[cel_widget_id="MAIN-SEARCH_RESULTS-9"]')
        third_product.click()

        #seçilen ürün başlığını kontrol ediyoruz.
        product_title = self.product_page.get_product_title()
        self.assertTrue(product_title.strip() != "")

        #seçilen ürünü sepete ekliyoruz.
        self.product_page.add_to_cart()

        #sepet sayacını kontrol ediyoruz.
        cart_count = self.product_page.get_cart_count()
        self.assertEqual(cart_count, "1")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()