# Company Information Scraper

This Python script helps to retrieve company information from the Taiwan Business Registration Database (商工登記公示資料查詢服務).

## Features

- Searches company information using Unified Business Number (統一編號)
- Saves company information to CSV file
- Includes company details such as:
  - Company Name
  - Registration Number
  - Registration Authority
  - Registration Status
  - Address
  - Establishment Date
  - Last Update Date

## Requirements

- Python 3.x
- Selenium
- pandas
- webdriver_manager

## Installation

1. Clone this repository
2. Install required packages:
```bash
pip install selenium webdriver-manager pandas
```

## Usage

1. Run the script with Python:
```bash
python company_search.py
```

2. The script will automatically:
   - Open the business registration website
   - Search for the company information
   - Save the results to a CSV file

## Note

This script is for educational purposes only. Please respect the website's terms of service and usage policies.
