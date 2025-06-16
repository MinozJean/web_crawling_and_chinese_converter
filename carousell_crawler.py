import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from chinese_converter import converter

def carousell_crawler():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        url = "https://tw.carousell.com/categories/women-s-fashion-4/"
        driver.get(url)

        input("Click 'Show more results' button on the page as many time as you want.\nPress ENTER when finish......\n")

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        products = soup.select("div.D_ps")

        output = []
        for product in products:
            try:
                traditional = product.select_one('p.D_jg.D_ju').get_text()
                price = product.select_one('p.D_jt').get_text().split('(')[0].strip()
                simplified = converter(traditional)
                output.append([traditional, simplified, price])
            except Exception:
                print("A product has some issues.(Skip)")
                continue

        with open('output.csv', 'w', newline='', encoding='utf-8') as myfile:
            wr = csv.writer(myfile)
            wr.writerow(["Traditional Chinese", "Simplified Chinese", "Price"])
            wr.writerows(output)

        print("Successfully save to output!")
    except Exception:
        print("Can't load the website (or accidently closs the page before press ENTER).")
    finally:
        driver.quit()