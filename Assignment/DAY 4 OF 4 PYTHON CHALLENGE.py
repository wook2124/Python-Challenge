import os
import requests

os.system("clear")
clear = os.unlink

print("Welcome to IsItDown.py!")
print("Please write a URL or URLs you want to check. (separated by comma)")

URL = input("")
r = requests.get(URL)
r.status_code == requests.codes.ok
URL.strip()
URL.split()
# try, except

qestion = input("Do you want to start over? y/n")
qestion
y = "y"
n = "n"
if qestion == y:
  clear()
elif qestion == n:
  print("See you on the Next Request!")
else:
  print("That's invalid answer!")
