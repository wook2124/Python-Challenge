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
rows = table.find_all("tr")[1:]

# print(rows)

for row in rows:
    data = row.find_all("td")
    # name = Country name
    name = data[0].text
    code = data[2].text
    if name and code:
        if name != "No universal currency":
            country = {'name': name.capitalize(), 'code': code}
            countries.append(country)


def restart():
  answer = str(input("Do you want to find more? y/n ")).lower()
  if answer == "y" or answer == "n":
    if answer == "y":
      ask()
    else:
      print("OK. Bye!")
      return
  else:
    print("That's not a valid answer. Please answer `y` or `n`")
    restart()


def ask():
    try:
        # choose index_value
        choice = int(input("#: "))
        if choice > len(countries):
            print("Choose a number from the list.")
            ask()
        else:
            country = countries[choice]
            print(f"Country: {country['name']}🌏")
            print(f"Currency: {country['code']}💲")
            restart()
    # input result = not int
    except ValueError:
        print("That wasn't a number. Please wirte a number.")
        ask()


print("Hello! Please choose select a country by number:")
# enumerate = 열거하다 / 기본적으로 인덱스 값을 포함해서 출력함
for index_value, country in enumerate(countries):
    print(f"#{index_value} {country['name']}")

ask()
