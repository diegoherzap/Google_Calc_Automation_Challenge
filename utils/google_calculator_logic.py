import logging
import time

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logger = logging.getLogger(__name__)


def wait_until_element_visible_and_clickable(google_calc_page, button_text, driver, timeout=10):
    locator = google_calc_page.locators.get(button_text)
    try:
        # Wait until the element visible
        element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
        logger.info("Google calculator screen is ready for interaction.")
        return element
    except TimeoutException:
        logger.exception("Timed out waiting for element to be clickable.")
        return None


def parse_number_or_operator_and_click(google_cal_page, number_or_operator):
    # Convert number or operator to string
    number_or_operator_to_string = str(number_or_operator)
    # Convert string to iterable
    iterable = list(number_or_operator_to_string)
    # This variable will later determine if the number is negative and the logic will follow accordingly
    negative = False
    # Click each character using the GoogleCalculatorPage instance
    if len(iterable) >= 2:
        for char in iterable:
            if char == "-":
                negative = True
                continue
            click_button(google_cal_page, char)
            time.sleep(0.2)  # Delay between clicks
            logger.info(f"Clicked '{char}' button.")
    else:
        click_button(google_cal_page, iterable[0])
        time.sleep(0.2)  # Delay between clicks
        logger.info(f"Clicked '{iterable[0]}' button.")

    if negative:
        click_button(google_cal_page, "+/-")


# Click a button (By) related to the passed char
def click_button(google_cal_page, button_text):
    locator = google_cal_page.locators.get(button_text)
    if locator:
        google_cal_page.driver.find_element(*locator).click()
    else:
        print(f"Locator for char {button_text} does not exist!")


# Get text from calculator screen
def get_result(google_cal_page):
    result = google_cal_page.driver.find_element(*google_cal_page.calculator_display).text
    return result
