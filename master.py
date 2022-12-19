import requests
from bs4 import BeautifulSoup
from lxml import etree as et
import time
import random
import csv

URL = "https://www.amazon.it/ASUS-DisplayPort-Overclock-Consigliata-Illuminazione/dp/B096SF185K/"
HEADERS = ({
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 44.0.2403.157 Safari / 537.36',
    'Accept-Language': 'it-IT, it, q=0.5'})

paginaweb = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(paginaweb.content, "lxml")

Nomeprodotto = ''
PrezzoProdotto = ''

try:

    Titoloprodotto = soup.find("span", attrs={"id": 'productTitle'})
    Nomeprodotto = Titoloprodotto.string.strip()

except AttributeError:
    Nomeprodotto = 'NA'

try:

    PrezzoProdotto = soup.find(
        "span", attrs={"class": 'a-offscreen'}).string.strip().replace('€', '')

except AttributeError:
    PrezzoProdotto = 'NA'

print("Titolo Prodotto:" + Nomeprodotto)
print("Prezzo:" + PrezzoProdotto)
