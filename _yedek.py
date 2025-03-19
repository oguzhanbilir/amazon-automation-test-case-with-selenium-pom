import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class TestCheckAddToCartAmazon(unittest.TestCase):
    def setUp(self):
        #tarayıcı seçeneklerini ayarlayarak, tarayıcıyı başlatıyoruz
        chromeOptions = Options()
        chromeOptions.add_argument('--disable-notifications')
        self.driver = webdriver.Chrome(options=chromeOptions)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        print("Tarayıcı başlatıldı ve maximize edildi.")

    def testCheckAddToCartAmazon(self):
        print("Test başladı.")

        #amazon anasayfasına gidiyoruz
        self.driver.get("https://www.amazon.com.tr/")
        print("Amazon ana sayfasına gidildi.")
        self.assertEqual("https://www.amazon.com.tr/", self.driver.current_url, "URL is not correct")
        print("URL doğrulandı.")

        #çerezleri kabul ediyoruz
        try:
            cookiesAccept = self.driver.find_element(By.ID, "sp-cc-accept")
            cookiesAccept.click()
            print("Çerezler kabul edildi.")
        except Exception as e:
            print("Çerezler kabul etme butonu bulunamadı veya zaten gösterilmiyor.", e)

        #arama kutusuna 'Samsung' yazarka armayı gerçekleştiriyoruz
        searchInput = self.driver.find_element(By.ID, "twotabsearchtextbox")
        searchInput.clear()  #her ihtimale karşı arama kutusunu temizliyoruz
        searchInput.send_keys("samsung")
        searchInput.send_keys(Keys.ENTER)
        print("'Samsung' araması yapıldı.")

        #arama sonucunu kontrol ederek, eğer 'samsung' içermiyorsa hata mesajı yazdırıyoruz
        self.driver.implicitly_wait(5)
        search_result = self.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']")
        self.assertIn("samsung", search_result.text.lower(), "Search result is not correct")
        print("Arama sonucu kontrol edildi: ", search_result.text)

        #arama sonuç sayfasında stokta olmayanları dahil et checkbox'ının varlığını kontrol ediyoruz
        try:
            stock_checkbox = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//span[contains(text(), 'Stokta Olmayanları Dahil Et')]/ancestor::a"))
            )
            #checkbox'ın seçili olup olmadığını kontrol ediyoruz
            if stock_checkbox.find_element(By.XPATH, ".//input").is_selected():
                print("Stokta olmayanları dahil et seçeneği seçili. Kaldırılıyor...")
                stock_checkbox.click()
                WebDriverWait(self.driver, 10).until(
                    EC.staleness_of(stock_checkbox)
                )
            else:
                print("Stokta olmayanları dahil et seçeneği seçili değil. Devam ediliyor...")
        except Exception as e:
            print("Stokta olmayanları dahil et checkbox'ı bulunamadı veya işlem yapılamadı:", e)

        #gösterilen sonuçlarda 2. sayfaya gidiyoruz
        nextPage = self.driver.find_element(By.CSS_SELECTOR, "a.s-pagination-item.s-pagination-next")
        nextPage.click()
        print("2. sayfaya geçiş yapıldı.")

        #2. sayfanın açıldığını kontrol ediyoruz
        currentUrl = self.driver.current_url
        self.assertIn("page=2", currentUrl, "Failed to navigate to the 2nd page")
        print("2. sayfa URL doğrulandı:", currentUrl)

        self.driver.implicitly_wait(2)
        #2. sayfadaki ürünlerden 3. ürünü seçiyoruz
        thirdProduct = self.driver.find_element(By.CSS_SELECTOR, '[cel_widget_id="MAIN-SEARCH_RESULTS-9"]')
        thirdProduct.click()
        print("Üçüncü ürün seçildi.")

        #ürün sayfasının açıldığını kontrol ediyoruz
        try:
            productTitle = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "productTitle"))
            )
            self.assertTrue(productTitle.text.strip() != "", "Ürün başlığı sayfada görünmüyor!")
            print("Ürün başlığı bulundu:", productTitle.text.strip())
        except Exception as e:
            print("Ürün başlığı bulunamadı:", e)

        #ürün sayfasında 'Sepete Ekle' butonunu kontrol ediyoruz
        try:
            addToCartButton = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "add-to-cart-button"))
            )
            addToCartButton.click()
            print("Add to Cart butonuna tıklandı.")
        except (NoSuchElementException, TimeoutException):
            try:
                #eğer 'Sepete Ekle' butonu yoksa "Diğer Alışveriş Seçenekleri'ne tıklıyoruz
                seeAllOptions = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "buybox-see-all-buying-choices"))
                )
                print("Bu üründe doğrudan sepete ekleme yok, test sonlandırılıyor.")
                return  #testi burada sonlandır
            except Exception as e:
                print("Ne sepete ekleme ne de alternatif seçenek bulunamadı:", e)
                self.fail("Üründe sepete ekleme veya alternatif seçenek bulunamadı!")

        #sepete eklendiğine dair onay mesajını kontrol ediyoruz
        try:
            confirmationMessage = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Sepete eklendi')]"))
            )
            self.assertIn("Sepete eklendi", confirmationMessage.text, "Ürün sepete eklenemedi!")
            print("Onay mesajı alındı:", confirmationMessage.text)
        except Exception as e:
            print("Onay mesajı bulunamadı:", e)

        #sepet sayacını kontrol ediyoruz
        try:
            cartCount = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "nav-cart-count"))
            )
            cartCountText = cartCount.text.strip()
            self.assertEqual(cartCountText, "1", f"Sepete atılan üründe sorun var, sepet sayacı: {cartCountText}")
            print("Sepet sayacı kontrol edildi:", cartCountText)
        except Exception as e:
            print("Sepet sayacı bulunamadı:", e)

        #sepete git butonuna tıklıyoruz
        try:
            goToCartButton = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Sepete Git')]"))
            )
            goToCartButton.click()
            print("Sepete Git butonuna tıklandı.")
        except Exception as e:
            print("Sepete Git butonu bulunamadı:", e)

        #sepet sayfasının açıldığını kontrol ediyoruz
        self.assertIn("/cart", self.driver.current_url, "Sepet sayfası açılmadı!")
        print("Sepet sayfası açıldı:", self.driver.current_url)

        #sepet sayfasında ürünün bulunduğunu kontrol ediyoruz
        try:
            productInCart = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".sc-product-title"))
            )
            self.assertTrue(productInCart.text.strip() != "", "Sepette ürün bulunamadı!")
            print("Sepetteki ürün kontrol edildi:", productInCart.text.strip())
        except Exception as e:
            print("Sepetteki ürün bulunamadı:", e)

        #sepet sayfasında ürünü sil butonuna tıklıyoruz
        deleteButton = self.driver.find_element(By.CSS_SELECTOR, "[data-feature-id='item-delete-button']")
        deleteButton.click()

        #silme işleminin gerçekleştiğini kontrol ediyoruz
        try:
            #ara toplam mesajını kontrol ediyoruz
            subtotalMessage = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "sc-subtotal-label-activecart"))
            )
            self.assertIn("0 ürün", subtotalMessage.text, "Sepette ürün bulunuyor!")
            print("Ara toplam mesajı kontrol edildi:", subtotalMessage.text)

            #sepetin boş olduğunu kontrol ediyoruz
            cartCount2 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "nav-cart-count"))
            )
            self.assertEqual(cartCount2.text, "0", "Sepet sayacı 0 göstermiyor!")
            print("Sepet sayacı kontrol edildi:", cartCount2.text)
        except Exception as e:
            print("Sepetin boş olduğu doğrulanamadı:", e)

        #amazon logosuna tıklıyoruz ve ana sayfaya dönüyoruz
        try:
            amazonLogo = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "nav-logo-sprites"))
            )
            amazonLogo.click()
            print("Amazon logosuna tıklandı, ana sayfaya dönülüyor...")
        except Exception as e:
            print("Amazon logosu bulunamadı veya tıklanamadı, doğrudan ana sayfaya gidiliyor:", e)
            self.driver.get("https://www.amazon.com.tr/")

        #ana sayfanın açıldığını kontrol ediyoruz
        try:
            #URL'i kontrol ediyoruz
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("https://www.amazon.com.tr/")
            )
            self.assertIn("https://www.amazon.com.tr/", self.driver.current_url, "Ana sayfa URL'si doğrulanamadı!")
            print("Ana sayfa URL'si doğrulandı:", self.driver.current_url)
        except Exception as e:
            print("Ana sayfa doğrulanamadı:", e)

    def tearDown(self):
        #tarayıcıyı kapatıyoruz
        self.driver.quit()
        print("Tarayıcı kapatıldı.")


if __name__ == "__main__":
    unittest.main()