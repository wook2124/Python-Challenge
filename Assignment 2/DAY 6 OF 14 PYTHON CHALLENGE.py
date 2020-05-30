import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

code_url = "https://www.iban.com/currency-codes"

code_request = requests.get(code_url)
code_soup = BeautifulSoup(code_request.text, "html.parser")

# table class = table table-bordered downloads tablesorter
table = code_soup.find("table")
# th(thead), tbody >> tr(table row) >> td(table data)
# td[0] = th - Country, Currency, Code, Number
# td[1~] = tb - Value
# td[0:3] = print(td[0, 1, 2])
rows = table.find_all("tr")[1:]

countries = []

for row in rows:
  data = row.find_all("td")
  # name = Country name
  name = data[0].text
  # code = Currency code
  code = data[2].text
  if name and code:
    # No universal currency = Currency code is empty
    if name != "No universal currency":
        country = {'name': name.capitalize(), 'code': code}
        countries.append(country)

print("Welcome to CurrencyConvert PRO 2020\n")
# enumerate = 열거하다 / 기본적으로 인덱스 값을 포함해서 출력함
for index_value, country in enumerate(countries):
  print(f"#{index_value} {country['name']}")


def ask_country(text):
  print(text)
  try:
    # choose index_value
    choice = int(input("#: "))
    if choice > len(countries):
      print("Choose a number from the list.")
      return ask_country(text)
    else:
      print(f"{countries[choice]['name']}")
      return countries[choice]
  except ValueError:
    print("That wasn't a number. Please wirte a number.")
    return ask_country(text)
    

def ask_amount(a_country, b_country):
  try:
    print(f"\n\nHow many {a_country['code']} do you want to convert to {b_country['code']}?")
    amount = int(input())
    return amount
  # input result = not int
  except ValueError:
    print("That wasn't a number. Please wirte a number.")
    return ask_amount(a_country, b_country)


user_country = ask_country("\n\nWhere are you from? Choose a country by number.")
target_country = ask_country("\n\nNow choose another country.")

amount = ask_amount(user_country, target_country)


# 환전 사이트
currency_url = "https://transferwise.com/gb/currency-converter/"

# code 값
user_code = user_country['code']
target_code = target_country['code']

# KRW => USD 10000원 환전 url = {https://transferwise.com/gb/currency-converter/}{krw}-to-{usd}-rate?amount={10000}
currency_request = requests.get(f"{currency_url}{user_code}-to-{target_code}-rate?amount={amount}")
currency_soup = BeautifulSoup(currency_request.text, "html.parser")
# 환전한 amount를 보여주는 input란을 가지고옴
currency_result = currency_soup.find("input", {"id": "cc-amount-to"})
if currency_result:
  currency_result = currency_result['value']
  # 처음에 입력한 amount
  amount = format_currency(amount, user_code, locale="ko_KR")
  # 환전해서 나온 amount
  currency_result = format_currency(currency_result, target_code, locale="ko_KR")
  print(f"{amount} is {currency_result}")
