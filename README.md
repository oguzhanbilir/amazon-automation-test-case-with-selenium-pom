# Amazon Automation Test Case with Selenium (POM)

Bu proje, Amazon web sitesi üzerinde Selenium ve Page Object Model (POM) kullanarak otomasyon testleri gerçekleştirmek için oluşturulmuştur.

## 📦 Kurulum

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları takip edin.

### Gereksinimler
- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)

### Adımlar
1. Projeyi klonlayın:
   ```bash
   git clone https://github.com/oguzhanbilir/amazon-automation-test-case-with-selenium-pom.git

2. Proje dizinine gidin:
   ```bash
   cd amazon-automation-test-case-with-selenium-pom

3. Gerekli bağımlılıkları yükleyin:
   ```bash
   pip install -r requirements.txt

4. Projeyi çalıştırmak için aşağıdaki komutu kullanın:
   ```bash
   python -m unittest tests/test_check_add_to_cart_amazon.py

Bu komut, Amazon üzerinde sepete ürün ekleme test senaryosunu çalıştıracaktır.

🧪 Testler
Projede aşağıdaki test senaryoları bulunmaktadır:

Amazon ana sayfasını açma

Çerezleri kabul etme

Arama kutusuna ürün girme ve arama yapma

Arama sonuçlarında 2. sayfaya geçme

Belirli bir ürünü sepete ekleme

Sepet sayacını kontrol etme

Testleri çalıştırmak için:

   ```bash
   python -m unittest discover tests
