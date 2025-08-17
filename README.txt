Project Descriptions:
This project creates a Chinese Converter converting Traditional Chinese to Simplified Chinese, and extracts the product titles and prices from the Carousell website.

File Descriptions:
1. main.py
    -> Entry point of the program.
    -> Call function from carousell_crawler.py to start crawling.
2. carousell_crawler.py
    -> Extract product titles and prices from the Carousell "Women's Fashion" category.
    -> If user clicks "Show more results" button on the browser, it dynamically loads more products, which will also finally save to output.
    -> Output datas to a CSV file "output.csv".
3. chinese_converter.py
    -> Convert Traditional Chinese to Simplified Chinese using a dictionary based on Wikimedia's php file.

Installation:
require python 3.x
pip3 install requests
pip3 install selenium
pip3 install beautifulsoup4

How to Run:
1. Run main.py in a terminal or code editor.
2. The browser window would open. You may click the "Show more results" button manually as many times as you want.
3. Make sure don't close the browser while the script is running.
4. Press ENTER in the terminal to stop execution.
5. A csv file with product datas will be saved to the project directory.
