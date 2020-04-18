import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

URL = "https://www.iban.com/currency-codes"

countries = []

request = requests.get(URL)
soup = BeautifulSoup(request.text, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")[1:]

for row in rows:
  items = row.find_all("td")
  name = items[0].text
  code = items[2].text
  if name and code:
    if name != "No universal currency.":
      country = {
        "name": name.capitalize(),
        "code": code
      }
      countries.append(country)

def ask():
  try:
    choice = int(input("#: "))
    if choice > len(countries):
      print("Choose a number from the list.")
      ask()
    else:
      country = countries[choice]
      print(f"{country['name']}")
      print("\nNow choose another country.\n")
    try:
      choice = int(input("#: "))
      if choice > len(countries):
        print("Choose a number from the list.")
        ask()
      else:
        country = countries[choice]
        print(f"{country['name']}")
        print(f"\nHow many {country['code']} do you want to convert to {country['code']}?")
        AMOUNT = int(input(""))
        convert = format_currency(f"{AMOUNT}, {country['code']}, {country['name']}")
        return convert
        print(f"{country['code']}{AMOUNT} is ")
    except ValueError:
      print("That wasn't a number.")
      ask()
  except ValueError:
    print("That wasn't a number.")
    ask()

print("Welcome to Currency-Convert PRO 2020\n")
for index, country in enumerate(countries):
  print(f"#{index} {country['name']}")

print("\nWhere are you from? Choose a country by number.\n")

ask()
