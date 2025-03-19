# Amazon Automation Test Case with Python+Selenium 

This project was developed to automate the testing of Amazon's website using Selenium and the Page Object Model (POM).

https://www.loom.com/share/698033f81e8441a6bae5f47228cc3f57

<b>PAGE</b>

pages > base_page.py
This file provides a basic structure for all other page classes. Common operations with Selenium WebDriver, such as checking for the existence of an element or waiting for page load, are defined here. Other page classes inherit from this class and utilize these shared functions.

pages > home_page.py
This role is responsible for managing operations related to Amazon's home page. It encompasses various operations, such as text entry in the search bar and clicking on specific elements on the home page.

pages > product_page.py
This role is responsible for managing the operations related to the detail page of a product. This section details operations such as adding a product to a cart and retrieving product information.

pages > search_results_page.py
This role is responsible for managing operations related to the search results page. This section details the process of selecting a specific product, filtering search results, and related tasks.

test > test_check_add_to_cart_amazon.py
This file contains a test case that evaluates the process of adding products to the cart. The scenario performs a search, selects, and adds a product to the cart using other page classes (e.g., home_page.py, search_results_page.py, product_page.py). The outcome of this process is then assessed to determine the success of the addition to the cart.

<b>STEPS</b>
1. Launch the Chrome browser.
2. Disable notifications.
3. Make the browser window full screen.
4. Set the time the browser waits to find the elements to 10 seconds.
5. Go to https://www.amazon.com.tr/.
6. Verify that the home page opens.
7. Click on the Accept cookies button if you have one and accept cookies.
8. Type “samsung” in the search box and click the search button.
9. Verify that the search results contain the word “samsung”.
10. Click on page 2 in the search results.
11. Verify that you are on page 2 by checking that the URL contains the phrase “page=2”.
12. Click on the 3rd product (element 9) on page 2.
13. Verify that the product page opens and the product title is not empty.
14. If the “Add to Cart” button is visible, click on it.
15. If the “Add to Cart” button is not visible, click on the “View Purchase Options” button and then click on the “Add to Cart” button.
16. Verify that the product has been added to the cart by checking that the cart counter is “1”.
17. Go to the cart page.
18. Verify that you are on the cart page and the correct product has been added to the cart.
19. Delete the product from the cart.
20. Verify that the product has been deleted from the cart.
21. Go back to the home page.
22. Verify that you are on the home page.
23. Close the browser when the test is complete.

<b>PROCESS SUMMARY<b/>

First, I ran the test steps manually. Then, using what I learned in test automation session 1 during the bootcamp process, I coded it in a complex single page with the name 'test_check_add_to_cart_amazon.py'. Then, using the Page Object Model (POM) structure I learned in test automation session 2, I decomposed the classes into pages. Finally, I completed the project by running automation tests.

