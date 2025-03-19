# Amazon Automation Test Case

This project contains automated test cases for Amazon's website. The tests are written in Python and use Selenium for browser automation.

## Prerequisites

- Python 3.x
- pip (Python package installer)
- Google Chrome browser
- ChromeDriver

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/oguzhanbilir/amazon-automation-test-case-with-selenium-pom.git
    cd amazon-automation-test-case-with-selenium-pom
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Download the ChromeDriver and ensure it is in your PATH. You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

## Running the Tests

To run the tests, execute the following command:
```sh
python -m unittest discover -s tests
```

## Project Structure

- `tests/`: Contains the test cases.
- `pages/`: Contains the page object models.
- `utils/`: Contains utility functions and helpers.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.