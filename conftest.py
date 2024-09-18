import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from tests.config import BASE_URL
from selenium.webdriver.chrome.service import Service
from page_objects.google_calculator_objects import GoogleCalculatorPage

@pytest.fixture(scope="class")
def driver():
    # Driver setup
    chrome_options = webdriver.ChromeOptions()
    chrome_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.maximize_window()

    # Open URL
    driver.get(BASE_URL)

    # Yield driver to the test
    yield driver

    # Teardown
    driver.quit()

@pytest.fixture(scope="class")
def google_cal_page(driver):
    # Initialize GoogleCalculatorPage with the driver and return the instance
    return GoogleCalculatorPage(driver)
