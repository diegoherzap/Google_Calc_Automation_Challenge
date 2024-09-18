from selenium.webdriver.common.by import By


class GoogleCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = {
                    "0": (By.ID, "view33"),
                    "1": (By.ID, "view25"),
                    "2": (By.ID, "view27"),
                    "3": (By.ID, "view29"),
                    "4": (By.ID, "view19"),
                    "5": (By.ID, "view21"),
                    "6": (By.ID, "view23"),
                    "7": (By.ID, "view13"),
                    "8": (By.ID, "view15"),
                    "9": (By.ID, "view17"),
                    ".": (By.ID, "view31"),  # Decimal point
                    "/": (By.ID, "view39"),  # Division
                    "*": (By.ID, "view41"),  # Multiplication
                    "-": (By.ID, "view43"),  # Subtraction or minus
                    "+": (By.ID, "view45"),  # Addition
                    "=": (By.ID, "view35"),  # Equals
                    "+/-": (By.ID, "view73"), # Negative
                    "CE": (By.ID, "view37")  # Clear Entry
                }

        # Calculator display
        self.calculator_display = (By.CLASS_NAME, "calculator-display")