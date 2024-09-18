import operator
from decimal import Decimal

operator_map = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}


def round_up_decimal(value, decimals=12):
    # Convert the value to a Decimal for precision
    value_decimal = Decimal(value)

    # Convert the value to a string for easier analysis of decimal places
    value_str = str(value_decimal)

    # If there's a decimal part, split the integer and fractional parts
    if '.' in value_str:
        integer_part, decimal_part = value_str.split('.')
        if len(decimal_part) >= 12:
            decimal_part = decimal_part[:12]  # Limited by Google Calculator

        # Iterate through the decimal part to find where repeating numbers start
        last_unique_index = 0
        for i in range(1, len(decimal_part)):
            if decimal_part[i] != decimal_part[i - 1]:
                last_unique_index = i

        # Now check if the following numbers are repeated or zeros
        repeated = True
        for i in range(last_unique_index + 1, min(last_unique_index + 12, len(decimal_part))):
            if decimal_part[i] != decimal_part[last_unique_index] and decimal_part[i] != '0':
                repeated = False
                break

        # If we have trailing zeros after the last unique number, truncate to that point
        if repeated and decimal_part[last_unique_index] == '0':
            return f"{integer_part}.{decimal_part[:last_unique_index]}"

        # Otherwise, round to the specified number of decimal places
        return f"{integer_part}.{decimal_part[:decimals]}"

    # If there's no decimal part, return the integer as is
    return value_decimal if value_decimal % 1 != 0 else int(value_decimal)
