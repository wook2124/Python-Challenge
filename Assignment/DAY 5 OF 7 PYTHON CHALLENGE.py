import os
import requests
from bs4 import BeautifulSoup

os.system("clear")

def extract_currency_codes():
  URL = requests.get("https://www.iban.com/currency-codes")

  soup = BeautifulSoup(URL.text, "html.parser")

  table = soup.find("table", {"class": "table table-bordered downloads tablesorter"})

  links = table.find_all("tr")
  tds = []

  for link in links[1:-1]:
    tds.append(link.find("td").string)
  return tds


print(extract_currency_codes())


# ints = [8, 23, 45, 12, 78]
# for i in ints:
#     print(f"item #{} = {}".format(???, i))

# for idx, val in enumerate(ints):
#     print(idx, val)