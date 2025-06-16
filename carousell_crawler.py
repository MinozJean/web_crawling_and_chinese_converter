import requests
import csv
from bs4 import BeautifulSoup
from chinese_converter import converter

def carousell_crawler():
    url = "https://tw.carousell.com/categories/women-s-fashion-4/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/136.0.0.0 Safari/537.36",
        "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        products = soup.select('div.D_ps')
        output = []
        print("Start converting Chinese from Carousell website......")

        for product in products:
            name = product.select_one('p.D_jg.D_ju')  
            price = product.select_one('p.D_jt')
            traditional = name.get_text(strip=True)
            price = price.get_text(strip=True)
            simplified = converter(traditional)
            output.append([traditional, simplified, price])

        with open('output.csv', 'w', newline='', encoding='utf-8') as myfile:
            wr = csv.writer(myfile)
            wr.writerow(["Traditional Chinese", "Simplified Chinese", "Price"])
            wr.writerows(output)

        print("Successfully save to output!")
    else:
        print("Can't load the website.")