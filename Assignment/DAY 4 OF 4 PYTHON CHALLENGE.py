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


# 정답 #
import os
import requests

def restart():
  answer = str(input("Do you want to start over? y/n ")).lower()
  if answer == "y" or answer =="n":
    if answer == "n":
        print("k. bye!")
        return
    elif answer == "y":
      main()
  else:
    print("That's not a valid answer")
    restart()


def main():
  os.system('clear')
  print("Welcome to IsItDown.py!\nPlease write a URL or URLs you want to check. (separated by comma)")
  urls = str(input()).lower().split(",")
  for url in urls:
    url = url.strip()
    if "." not in url:
      print(url, "is not a valid URL.")
    else:
      if "http" not in url:
        url = f"http://{url}"
      try:
        request = requests.get(url)
        if request.status_code == 200:
          print(url,"is up!")
        else:
          print(url, "is down!")
      except:
          print(url, "is down!")
  restart()


main()