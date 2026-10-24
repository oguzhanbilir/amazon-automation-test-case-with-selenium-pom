Türkçe | [English](README.md)

# Amazon sepete ekleme test otomasyonu (Python + Selenium)

Insider & Testinium Tech Hub QA Tester Bootcamp (2025) bitirme projemdir. amazon.com.tr üzerinde sepete ekleme akışını Selenium ve Page Object Model ile otomatikleştirir, pytest ile çalışır.

Demo videosu: https://www.loom.com/share/698033f81e8441a6bae5f47228cc3f57

## Çalıştırma

```bash
pip install -r requirements.txt
pytest --html=reports/report.html --self-contained-html
```

Chrome'u pencere açmadan çalıştırmak için `HEADLESS=1` verin. GitHub Actions her push'ta testleri headless çalıştırır ve HTML raporunu artifact olarak yükler.

Amazon, GitHub sunucuları gibi veri merkezi IP'lerine çoğu zaman mağaza sayfası yerine captcha gösterir. Bu durumda test geçti değil, nedeni yazılarak atlandı (skipped) olarak raporlanır. Senaryonun tamamı normal bir bilgisayarda çalışır.

## Yapı

```
pages/
  base_page.py            ortak beklemeler ve işlemler
  home_page.py            arama kutusu ve ana sayfa öğeleri
  search_results_page.py  sayfalama ve ürün seçimi
  product_page.py         ürün bilgisi ve sepete ekleme
  cart_page.py            sepetteki ürünü kontrol etme ve silme
tests/
  test_check_add_to_cart_amazon.py
.github/workflows/tests.yml
```

Tüm sayfa sınıfları, explicit wait'leri ve ortak işlemleri barındıran `BasePage` sınıfından türer. Test yalnızca sayfa sınıflarını kullanır.

## Test senaryosu

1. Chrome'u tam ekran ve bildirimler kapalı açar (explicit wait, öğe başına en fazla 10 sn)
2. https://www.amazon.com.tr/ adresine gider, ana sayfanın açıldığını doğrular; sorulursa çerezleri kabul eder
3. "samsung" araması yapar ve sonuçlarda bu kelimenin geçtiğini doğrular
4. Sonuçların 2. sayfasına geçer ve URL'de `page=2` olduğunu doğrular
5. 3. ürünü açar ve başlığın boş olmadığını doğrular; ürün stokta yoksa geri dönüp sıradakini dener
6. "Sepete Ekle"ye tıklar; buton görünmüyorsa önce "Satın alma seçeneklerini gör"e tıklar
7. Sepet sayacının 1 olduğunu doğrular
8. Sepete gider ve doğru ürünün eklendiğini doğrular
9. Ürünü siler ve sepetin boşaldığını doğrular
10. Ana sayfaya döner, doğrular ve tarayıcıyı kapatır

## Nasıl geliştirildi

Adımları önce elle denedim, sonra tek bir test dosyasında kodladım. Ardından kodu POM ile sayfa sınıflarına böldüm. Daha sonra sepet adımlarını da POM'a taşıdım, pytest ve HTML rapora geçtim ve GitHub Actions iş akışını ekledim.

Geliştirici: Oğuzhan Bilir
