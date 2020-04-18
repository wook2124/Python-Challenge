import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=JavaScript&radius=25&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

links = pagination.find_all("a")
spans = []
for link in links:
  spans.append(link.find("span"))

# 0부터 마지막 전(-2)까지 실행
spans = spans[0:-1]

print(spans)