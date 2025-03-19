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
        # Test başlamadan önce gerekli ayarlamaları yapıyoruz.
        chromeOptions = Options()
        chromeOptions.add_argument('--disable-notifications')

        # Chrome tarayıcısını başlatıyoruz ve pencereyi tam ekran yapıyoruz.
        self.driver = webdriver.Chrome(options=chromeOptions)
        self.driver.maximize_window()

        # Tarayıcının elementleri bulmak için bekleyeceği süreyi ayarlıyoruz.
        self.driver.implicitly_wait(10)

        # Sayfa class'ını başlatıyoruz.
        self.home_page = HomePage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.product_page = ProductPage(self.driver)

    def test_check_add_to_cart_amazon(self):
        # amazon.com.tr ana sayfasını açıyoruz.
        self.home_page.open()

        # Çerezleri kabul ediyoruz.
        self.home_page.accept_cookies()

        # Arama kutusuna 'Samsung' yazarak arama yapıyoruz.
        self.home_page.search_for("samsung")

        # Arama sonuçlarını kontrol ediyoruz.
        search_result_text = self.search_results_page.get_search_result_text()
        self.assertIn("samsung", search_result_text.lower())

        # Arama sonuçlarında 2. sayfaya geçiyoruz.
        self.search_results_page.go_to_next_page()
        self.assertIn("page=2", self.driver.current_url)

        # Arama sonuçlarında 2. sayfada üçüncü ürünü (9. element) seçiyoruz.
        third_product = self.driver.find_element(By.CSS_SELECTOR, '[cel_widget_id="MAIN-SEARCH_RESULTS-9"]')
        third_product.click()

        # Seçilen ürün başlığını kontrol ediyoruz.
        product_title = self.product_page.get_product_title()
        self.assertTrue(product_title.strip() != "")

        # Eğer "Sepete Ekle" butonu yoksa, "Satın Alma Seçeneklerini Gör" butonuna tıklayıp oradan sepete ekliyoruz.
        try:
            self.product_page.add_to_cart()
        except:
            # "Satın Alma Seçeneklerini Gör" butonuna tıklıyoruz.
            self.driver.find_element(By.CSS_SELECTOR, 'span.a-button-inner a[title="Satın Alma Seçeneklerini Gör"]').click()

            # "Sepete Ekle" butonuna tıklıyoruz.
            self.driver.find_element(By.CSS_SELECTOR, 'input[name="submit.addToCart"]').click()

        # Sepet sayacını kontrol ediyoruz.
        cart_count = self.product_page.get_cart_count()
        self.assertEqual(cart_count, "1")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()