#!/bin/bash

# Ensure the reports directory exists
mkdir -p reports

# Run pytest and generate the HTML report in the reports directory
pytest -m integral --html=reports/test_report.html --self-contained-html