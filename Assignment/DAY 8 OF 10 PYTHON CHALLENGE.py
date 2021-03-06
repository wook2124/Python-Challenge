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


# 정답 #
import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")


def write_company(company):
    file = open(f"{company['name']}.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "date"])
    for job in company["jobs"]:
      writer.writerow(list(job.values()))


alba_url = "http://www.alba.co.kr"

alba_request = requests.get(alba_url)
alba_soup = BeautifulSoup(alba_request.text, "html.parser")
main = alba_soup.find("div", {"id": "MainSuperBrand"})
brands = main.find_all("li", {"class": "impact"})
for brand in brands:
    link = brand.find("a", {"class": "goodsBox-info"})
    name = brand.find("span", {"class": "company"})
    if link and name:
        link = link["href"]
        name = name.text
        company = {'name': name, 'jobs': []}
        jobs_request = requests.get(link)
        jobs_soup = BeautifulSoup(jobs_request.text, "html.parser")
        tbody = jobs_soup.find("div", {"id": "NormalInfo"}).find("tbody")
        rows = tbody.find_all("tr", {"class": ""})
        for row in rows:
            local = row.find("td", {"class": "local"})
            if local:
                local = local.text.replace(u'\xa0', ' ')
            title = row.find("td", {"class": "title"})
            if title:
                title = title.find("a").find("span", {
                    "class": "company"
                }).text.strip()
                title = title.replace(u'\xa0', ' ')
            time = row.find("td", {"class": "data"})
            if time:
                time = time.text.replace(u'\xa0', ' ')
            pay = row.find("td", {"class": "pay"})
            if pay:
                pay = pay.text.replace(u'\xa0', ' ')
            date = row.find("td", {"class": "regDate"})
            if date:
                date = date.text.replace(u'\xa0', ' ')
            job = {
                "place": local,
                "title": title,
                "time": time,
                "pay": pay,
                "date": date
            }
            company['jobs'].append(job)
        write_company(company)