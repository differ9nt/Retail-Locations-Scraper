# Retail-Locations-Scraper
Scrapes EE store names and addresses from the-shops.co.uk using Selenium and saves them to a CSV.

This Python script uses Selenium to scrape store names and addresses from the EE (Everything Everywhere) store locator on the-shops.co.uk. It navigates through all paginated results, handles cookie consent, and exports the data into a CSV file (store_info.csv).

Features:
	•	Headless web scraping with selenium and webdriver-manager
	•	Waits dynamically for content to load using WebDriverWait
	•	Handles pagination and clicks through all result pages
	•	Outputs clean CSV with store names and addresses
