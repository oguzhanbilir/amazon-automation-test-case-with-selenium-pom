English | [Türkçe](README.tr.md)

# Amazon add-to-cart test automation (Python + Selenium)

This was my final project for the Insider & Testinium Tech Hub QA Tester Bootcamp (2025). It automates the add-to-cart flow on amazon.com.tr with Selenium and the Page Object Model, and runs with pytest.

Demo video: https://www.loom.com/share/698033f81e8441a6bae5f47228cc3f57

## Running

```bash
pip install -r requirements.txt
pytest --html=reports/report.html --self-contained-html
```

Set `HEADLESS=1` to run Chrome without a window. GitHub Actions runs the suite headless on every push and uploads the HTML report as an artifact.

Amazon often answers datacenter IPs, like GitHub's runners, with a captcha instead of the store page. When that happens the test is reported as skipped with that reason, not as passed. The full scenario runs on a normal machine.

## Structure

```
pages/
  base_page.py            shared waits and actions
  home_page.py            search box and home page elements
  search_results_page.py  paging and picking a product
  product_page.py         product details and add to cart
  cart_page.py            checking and removing the cart item
tests/
  test_check_add_to_cart_amazon.py
.github/workflows/tests.yml
```

Every page class inherits from `BasePage`, which holds the explicit waits and common actions. The test only talks to the page classes.

## Test scenario

1. Open Chrome full screen with notifications off (explicit waits, up to 10 s per element)
2. Go to https://www.amazon.com.tr/ and check the home page opened; accept cookies if asked
3. Search for "samsung" and check the results contain the word
4. Go to page 2 of the results and check the URL contains `page=2`
5. Open the 3rd product and check its title is not empty; if it's out of stock, go back and try the next one
6. Click "Add to Cart", or "See buying options" first if the button isn't shown
7. Check the cart counter shows 1
8. Open the cart and check the right product is there
9. Remove the product and check the cart is empty
10. Go back to the home page, check it, and close the browser

## How it was built

I first ran the steps by hand, then wrote them as a single test file. Next I split the code into page classes with POM. Later I moved the cart steps into POM too, switched the runner to pytest with an HTML report, and added the GitHub Actions workflow.

Developer: Oğuzhan Bilir
