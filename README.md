# Web Scraping and Data Compilation Scripts
## Overview

This repository contains two Python scripts designed to extract and compile data from the products catalogue of microorganisms on the DSMZ website (https://www.dsmz.de/collection/catalogue/microorganisms/catalogue). As of 10/06/2024, there were approximately 31,327 products listed on the website.

### Script 1: Web_scraping.py

The 'Web_scraping.py' script performs the following tasks:

1. Extracts product information from the DSMZ website.
2. Creates a new text file for each product.
3. Stores the extracted data in tab-separated format.
4. Saves each text file with the name corresponding to the product.

This process generates a total of 31,327 text files, each containing details of a specific product. An example of such a file has been uploaded for reference (`DSM-1.txt`).

### Script 2: txt_to_excel.py

The `txt_to_excel.py` script performs the following tasks:

1. Creates a new Excel sheet.
2. Appends information from all 31,327 text files into the Excel sheet.
3. Ensures that the Excel file contains data from all text files, resulting in a total of 31,328 rows (including the header).

The compiled Excel file (`dsmz_details.xlsx`) is also uploaded for reference.

#### Usage

To use these scripts, follow these steps:

1. Run 'Web_scraping.py' on command prompt to scrape data from the DSMZ website and generate text files for each product (python3 Web_scraping.py).
2. Run 'txt_to_excel.py' on command prompt to compile the data from the text files into a single Excel sheet (python3 txt_to_excel.py).

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
