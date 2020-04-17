import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
URL = requests.get("https://www.iban.com/currency-codes")

soup = BeautifulSoup(URL.text, "html.parser")

table = soup.find("table", {"class": "table table-bordered downloads tablesorter"})

pages = table.find_all("tr")
tds = []

for page in pages:
  tds.append(page.find("td"))

print(tds[1:-1])