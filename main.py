from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib
import datetime
import csv
import pandas as pd


# url = "https://www.amazon.com/OnePlus-Dual-SIM-Smartphone-Hasselblad-Processor/dp/B0BNWPSCGB/"


# print(title)
# print(price)
#
#
# print(today)


#
# with open('AmazonScraperData.csv', 'w', newline='', encoding='UTF8') as file:
#     write = csv.writer(file)
#     write.writerow(header)
#     write.writerow(data)


def check_price():
    url = "https://www.amazon.com/dp/B0BNWPSCGB"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en",
        "Upgrade-Insecure-Requests": "1"}  # https://httpbin.org/get
    page = requests.get(url, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text().strip()
    price = soup2.find('span', {'class': 'a-offscreen'}).get_text().strip()[1:]
    today = datetime.date.today()

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('AmazonScraperData.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


i = 0
while i < 5:
    check_price()
    time.sleep(5)
    i += 1

df = pd.read_csv(r'AmazonScraperData.csv')
print(df)
