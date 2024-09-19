#!/bin/bash

# Ensure the reports directory exists
mkdir -p reports

# Run pytest and generate the HTML report in the reports directory
pytest -m basic_operations --html=reports/test_report.html --self-contained-html