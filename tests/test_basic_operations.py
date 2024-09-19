import logging
import pytest

from tests.test_data import numeric_operations
from utils.google_calculator_logic import parse_number_or_operator_and_click, wait_until_element_visible_and_clickable, \
    get_result
from utils.math_helper import round_up_decimal, operator_map

logger = logging.getLogger(__name__)


@pytest.fixture
def operation(request):
    return request.param


@pytest.mark.basic_operations
@pytest.mark.parametrize("operation", numeric_operations, indirect=True)
def test_operations(operation, driver, google_cal_page):
    """
    The "parametrize" mark iterates lists of operations in the form of operand (x), operator, operand (y). This is
    test data, and it is imported from ./test_data.py. This test method uses the operands and operator to feed the UI
    interactions and obtaining the result. It will then take the result from the UI and compare it to the operations
    performed locally. The test will pass or fail after comparing the expected vs obtained result.
    :param operation: This specifies that an operation is being requested.
    :param driver: The ChromeDriver object.
    :param google_cal_page: The GoogleCalculatorPage object that contains button handling references.
    :return: None
    """
    x, operator, y = operation
    operation = [x, operator, y, "="]
    wait_until_element_visible_and_clickable(google_cal_page, "CE", driver)

    # Use the page object and the logic functions to input and calculate
    for operand_or_operator in operation:
        parse_number_or_operator_and_click(google_cal_page, operand_or_operator)

    # Get the result from the calculator
    result = get_result(google_cal_page)
    expected = operator_map[operator](x, y)
    if expected.is_integer():
        expected = int(expected)
    else:
        expected = round_up_decimal(expected)
    expected_string = str(expected)
    logger.info(f"Expected: {expected_string} - Actual: {result}")

    assert result == expected_string, f"Expected {expected_string}, but got {result}"
