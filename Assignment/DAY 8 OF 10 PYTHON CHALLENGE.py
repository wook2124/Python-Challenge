import requests
from bs4 import BeautifulSoup

URL = "http://www.alba.co.kr"
daiso = "http://daiso.alba.co.kr/job/brand/"

result = requests.get(daiso)
soup = BeautifulSoup(result.text, "html.parser")


def extract_job(whatever):
    place = whatever.find("div", {"class": "L_MyAd_woowayouth0"})

    title = whatever.find("span", {"class": "title"})

    time = whatever.find("span", {"class": "time"})

    pay = whatever.find("span", {"class": "number"})

    date = whatever.find("td", {"class": "regDate last"})
    

    return {
        "place":
        place,
        "title":
        title,
        "time":
        time,
        "pay":
        pay,
        "date":
        date
    }


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping page {page}")
        result = requests.get(daiso)
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "goodsList goodsJob"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
  last_page = []
  jobs = extract_jobs([last_page])
  return jobs