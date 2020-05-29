import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

countries = []

request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

# table class = table table-bordered downloads tablesorter
table = soup.find("table")

# th(thead), tbody >> tr(table row) >> td(table data) 
# td[0] = th - Country, Currency, Code, Number
# td[1~] = tb - Value
# td[0:3] = print(td[0, 1, 2])
rows = table.find_all("tr")[1:-2]

print(rows)