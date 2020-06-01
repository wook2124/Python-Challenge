import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")

def csv_company(company):
  # "회사이름.csv"로 wirte으로 저장되게함
  file = open(f"{company['name']}.csv", mode="w")
  wirter = csv.writer(file)
  wirter.writerow(["local", "title", "time", "pay", "date"])
  for job in company['jobs']:
    wirter.writerow(list(job.values()))


alba_url = "http://www.alba.co.kr"

request = requests.get(alba_url)
soup = BeautifulSoup(request.text, "html.parser")
# 슈퍼브랜드 채용정보
main = soup.find("div", {"id": "MainSuperBrand"})
brands = main.find_all("li", {"class": "impact"})
for brand in brands:
  link = brand.find("a", {"class": "goodsBox-info"})
  name = brand.find("span", {"class": "company"})
  if link and name:
    link = link["href"]
    name = name.text
    # company의 job 정보를 추가할 'jobs'를 미리 만들어둠
    company = {'name': name, 'jobs': []}

    # 브랜드 안 채용정보 가져오기
    b_request = requests.get(link)
    b_soup = BeautifulSoup(b_request.text, "html.parser")
    # 일반 채용정보
    info = b_soup.find("div", {"id": "NormalInfo"}).find("tbody")
    # tbody안에 있는 모든 table row를 일단 가지고옴
    t_rows = info.find_all("tr", {"class": ""})
    for row in t_rows:
      # 근무지(local)
      local = row.find("td", {"class": "local"})
      # text로 바꾸려하는데 "경기&nbsp;군포시"로 되있음
      if local:
        local = local.text
      
      # 회사명/업무내용(title)
      title = row.find("td", {"class": {"title"}})
      if title:
        title = title.find("a").find("span", {"class": {"company"}}).text.strip()
      
      # 근무시간(time)
      time = row.find("td", {"class": {"data"}})
      if time:
        time = time.text

      # 급여(pay)
      pay = row.find("td", {"class": {"pay"}})
      if pay:
        pay = pay.text

      # 등록일(regDate)
      date = row.find("td", {"class": {"regDate"}})
      if date:
        date = date.text

      job = {
        "local": local,
        "title": title,
        "time": time,
        "pay": pay,
        "date": date
      }
      company['jobs'].append(job)
    csv_company(company)