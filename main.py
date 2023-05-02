from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib

url = "https://www.amazon.in/OnePlus-Sonic-Black-128GB-Storage/dp/B0BSNP46QP/?_encoding=UTF8&pd_rd_w=u8wM4&content-id=amzn1.sym.22a42d01-0089-4fec-a28b-ec7a361d085f&pf_rd_p=22a42d01-0089-4fec-a28b-ec7a361d085f&pf_rd_r=34TDR1R9VRK5C381TPBZ&pd_rd_wg=Tq3zE&pd_rd_r=097a336e-eff1-47cf-ad80-c121bcac23ca&ref_=pd_gw_ci_mcx_mr_hp_d&th=1"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
           "Accept-Encoding": "gzip, deflate, br",
           "Accept-Language": "en-US,en",
           "Upgrade-Insecure-Requests": "1"}
page = requests.get(url, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
title = soup2.find(id='productTitle').get_text()
price = soup2.find(id='priceblock_ourprice').get_text()

print(title)
print(price)