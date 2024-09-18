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
