import os
import requests

os.system("clear")
clear = os.unlink
y = "y"
n = "n"

print("Welcome to IsItDown.py!")
print("Please write a URL or URLs you want to check. (separated by comma)")

URL = input("")
if ".com" not in input:
  print("You have to put '.com' inside your answer!")
else:
  print(f"https://{URL} is up!")
  qestion = input("Do you want to start over? y/n")

while True:
  if qestion == y:
    clear()
    continue
  elif qestion == n:
    print("See you on the Next Request!")
    break
  else:
    print("That's invalid answer!")

r = requests.get(URL)
r.status_code == requests.codes.ok
URL.strip()
URL.split()
# try, except
