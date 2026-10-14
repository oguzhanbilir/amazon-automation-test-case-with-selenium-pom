import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

class TestCheckAddToCartAmazon(unittest.TestCase):
    def setUp(self):
        # Test başlamadan önce gerekli ayarlamaları yapıyoruz.
        chromeOptions = Options()
        chromeOptions.add_argument('--disable-notifications')

        # CI ortamında (HEADLESS=1) tarayıcıyı ekransız çalıştırıyoruz.
        if os.getenv("HEADLESS") == "1":
            chromeOptions.add_argument('--headless=new')
            chromeOptions.add_argument('--window-size=1920,1080')
            chromeOptions.add_argument('--no-sandbox')
            chromeOptions.add_argument('--disable-dev-shm-usage')

        # Chrome tarayıcısını başlatıyoruz ve pencereyi tam ekran yapıyoruz.
        self.driver = webdriver.Chrome(options=chromeOptions)
        self.driver.maximize_window()

        # Sayfa class'larını başlatıyoruz.
        self.home_page = HomePage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)

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

        # 2. sayfadaki üçüncü üründen başlayarak sepete eklenebilen ilk ürünü seçiyoruz.
        # Canlı sitede stoklar değiştiği için 3. ürün her zaman satın alınabilir olmayabilir.
        for position in range(3, 8):
            self.search_results_page.select_product(position)

            # Seçilen ürün başlığını kontrol ediyoruz.
            product_title = self.product_page.get_product_title()
            self.assertTrue(product_title.strip() != "")

            if self.product_page.is_purchasable():
                break
            self.driver.back()
        else:
            self.fail("3-7. sıradaki ürünlerin hiçbiri sepete eklenebilir değil.")

        # Ürünü sepete ekliyoruz.
        self.product_page.add_to_cart()

        # Sepet sayacını kontrol ediyoruz.
        cart_count = self.product_page.get_cart_count()
        self.assertEqual(cart_count, "1")

        # Sepet sayfasına gidip ürünün sepette olduğunu kontrol ediyoruz.
        self.cart_page.open()
        self.assertIn("/cart", self.driver.current_url)
        self.assertTrue(self.cart_page.get_product_title().strip() != "")

        # Ürünü sepetten silip sayacın 0'a düştüğünü kontrol ediyoruz.
        self.cart_page.delete_first_item()
        self.assertEqual(self.cart_page.wait_until_cart_count_is("0"), "0")

        # Logoya tıklayıp ana sayfaya döndüğümüzü kontrol ediyoruz.
        self.cart_page.go_to_home_page()
        self.assertTrue(self.driver.current_url.startswith("https://www.amazon.com.tr/"))
        self.assertNotIn("/cart", self.driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
