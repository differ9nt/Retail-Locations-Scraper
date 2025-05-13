#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the specified URL
driver.get("https://www.the-shops.co.uk/chainstore/284-ee")

# Prepare to write data to CSV
with open('store_info.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Store Name', 'Address'])

    try:
        # Wait for the cookies consent button and click it
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "didomi-notice-agree-button"))
        )
        cookie_button.click()

        while True:
            # Wait until the <h2> elements are present
            h2_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, "h2"))
            )

            # Wait until the <div> elements with the specified class are present
            div_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "font-weight-light"))
            )

            # Loop through the <h2> elements and <div> elements and write to the CSV
            for h2, div in zip(h2_elements, div_elements):
                writer.writerow([h2.text.strip(), div.text.strip()])

            # Try to find the next page button in the bottom pagination
            next_page = driver.find_elements(By.CSS_SELECTOR, "li.numbers.active + li.numbers a")

            if next_page:
                next_page[0].click()  # Click on the next page link
                WebDriverWait(driver, 10).until(EC.staleness_of(h2_elements[0]))  # Wait for the page to load
            else:
                break  # No more pages

        print("Data scraped and saved to EEstore_info.csv")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()


# In[ ]:





# In[ ]:





# In[ ]:




