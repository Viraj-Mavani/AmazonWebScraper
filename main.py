from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib
import datetime
import csv
import pandas as pd


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

    if int(price) < 700:
        send_mail()


    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('AmazonScraperData.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    # server.starttls()
    server.ehlo()
    server.login('gmail', 'password')

    subject = "The product you want is below $700! Now is your chance to buy!"
    body = "Viraj, This is the moment we have been waiting for. Now is your chance to pick up the product of your dreams. Don't mess it up! Link here: https://www.amazon.com/dp/B0BNWPSCGB"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'gmail',
        msg
    )


days = 0
while days < 30:
    check_price()
    time.sleep(86400)
    days += 1

df = pd.read_csv(r'AmazonScraperData.csv')
print(df)