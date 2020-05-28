import os
import requests

def restart():
  answer = str(input("Do you want to start over? y/n ")).lower()
  if answer == "y" or answer == "n":
    if answer == "y":
      main()
    else:
      print("OK. Bye!")
      return
  else:
    print("That's not a valid answer. Please answer `y` or `n`")
    restart()


def main():
  os.system("clear")
  print("Welcome to IsItDown.py!\nPlease write a URL or URLs you want to check. (separated by comma)")
  URLs = str(input()).lower().split(",")
  for URL in URLs:
    URL = URL.strip()
    if "." not in URL:
      print(URL, "is not a valid URL.")
    else:
      if "http" not in URL:
        URL = f"http://{URL}"
      try:
        request = requests.get(URL)
        if request.status_code == 200:
          print(URL, "is up!")
        else:
          print(URL, "is down!")
      except:
        print(URL, "is down!")
  restart()

main()