# Amazon Automation Test Case with Python+Selenium 

This project was developed to automate the testing of Amazon's website using Selenium and the Page Object Model (POM).

Otomasyon sürecinin çalışma videosunu izlemek için <a href"https://www.loom.com/share/698033f81e8441a6bae5f47228cc3f57">tıklayınız</a>.


Steps :
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

