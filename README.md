# MT3_Google_Calc_Challenge
This repository contains a solution for automating tests for Google's online calculator using Selenium. It was created as part of a technical exercise for the MT3 interview process.

## Features
Automated testing of basic arithmetic operations: addition, subtraction, multiplication, and division.
Pytest integration with custom logic for interacting with Google's calculator interface.
Generates HTML reports and logs for test results.

## Project Structure
```
MT3_Google_Calc_Challenge/
├── page_objects/         # Contains the Page Object model for the calculator.
├── tests/                # Test cases for validating operations.
├── utils/                # Utility functions for browser interactions and logic.
├── conftest.py           # Pytest fixture setups for WebDriver and test environment.
├── pytest.ini            # Pytest configuration for logging and reporting.
├── README.md             # Project documentation.
├── requirements.txt      # Project dependencies.
├── run_tests.sh          # Shell script to execute tests and generate reports.

```
## Installation
1. Clone the repository:
```
git clone https://github.com/diegoherzap/MT3_Google_Calc_Challenge.git
```
2. Navigate to the project directory:
```
cd MT3_Google_Calc_Challenge
```
3. Install dependencies:
```
pip install -r requirements.txt
```
## Running Tests
1. Execute the Test Suite with:
```
./run_tests.sh
```
2. The test results will be published on the reports directory after the test run is complete.
## Reporting
* HTML Report: Located in reports/test_report.html after running tests.
* Logs: Available in reports/test_log.log.
## License
This project is licensed under a Custom Non-Commercial License. You are free to clone, use, and modify this code for personal and educational purposes only. Commercial use or redistribution of any form is not permitted. If you share or distribute this code, you must retain the original copyright notice.
