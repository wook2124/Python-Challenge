import requests
from bs4 import BeautifulSoup

URL = f"https://weworkremotely.com/remote-jobs/search?term=python"

# 어떤거 구해올지 살펴보기

result = requests.get(URL)
soup = BeautifulSoup(result.text, "html.parser")
html = soup.find("div", {"class": "jobs"})


def extract_job(html):
    title = html.find("span", {"class": "title"})
    company = html.find("span", {"class": "company"})
    location = html.find("span", {"class": "region company"})
    company.get_text(strip=True)
    location.get_text(strip=True)
    link = html.find_all("li", {"class": "feature"}).find_all("a")
    return {
        "title": title,
        "company": company.string,
        "location": location.string,
        "link": link
    }


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&pg={page + 1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def remote_jobs():
    jobs = extract_jobs()
    return jobs
