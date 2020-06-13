import requests
import csv
from bs4 import BeautifulSoup


def get_soup(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")

    return soup


def get_so_jobs(soup, URL):
    page_a = soup.find_all("a", class_="s-pagination--item")

    try:
        last_page = page_a[-2].find("span").string
    except:
        return []

    jobs = []

    for page in range(1):
        url = f"{URL}&pg={page+1}"
        soup = get_soup(url)
        contents = soup.find_all("div", class_="grid--cell fl1")

        for content in contents:
            company = content.find("h3").find("span").find(text=True).strip()
            title = content.find("a")["title"]
            location = content.find(
                "span", class_="fc-black-500").string.strip()
            ref = content.find("a")["href"]

            job_url = f"https://stackoverflow.com{ref}"
            jobs.append({"company": company, "title": title,
                         "location": location, "url": job_url})

    return jobs


def get_ww_jobs(soup):
    jobs = []
    counter = 0

    try:
        contents = soup.find("section", {"id": "category-2"}).find_all("li")
        length = len(contents) - 1
    except:
        return []

    for content in contents[:-1]:
        try:
            company = content.find("span", class_="company").string
            title = content.find("span", class_="title").string
            location = content.find("span", class_="region company").string
            ref = content.find_all("a")[-1]["href"]
            url = f"https://weworkremotely.com{ref}"
            jobs.append({"company": company, "title": title,
                         "location": location, "url": url})
            counter += 1
        except:
            continue

    return jobs


def get_rm_jobs(soup):
    jobs = []
    counter = 0

    try:
        t_content = soup.find("table", {"id": "jobsboard"})
        t_heads = t_content.find_all("thead")
    except:
        return []

    index = -1

    for head in t_heads:
        if head.find("h2").string == "Previously":
            break
        index += 1

    t_bodys = t_content.find_all(
        "td", class_="company position company_and_position")[:index]
    length = len(t_bodys)

    for body in t_bodys:
        ref = body.find("a")["href"]
        url = f"https://remoteok.io{ref}"
        title = body.find("h2").string
        company = body.find("h3").string
        location = "Remote Work"

        print(f"[{counter+1}/{length}] Scrapping from RM on progress.")
        counter += 1

        jobs.append({"company": company, "title": title,
                     "location": location, "url": url})

    return jobs


def get_jobs(searched_term):
    so_url = f"https://stackoverflow.com/jobs?r=true&q={searched_term}"
    ww_url = f"https://weworkremotely.com/remote-jobs/search?term={searched_term}"
    rm_url = f"https://remoteok.io/remote-dev+{searched_term}-jobs"

    jobs = []
    jobs.extend(get_so_jobs(get_soup(so_url), so_url))
    jobs.extend(get_ww_jobs(get_soup(ww_url)))
    jobs.extend(get_rm_jobs(get_soup(rm_url)))

    return jobs


def save(lists):
    with open("jobs.csv", mode="w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(["Company", "Title", "Location", "Link"])

        for l in lists:
            writer.writerow(list(l.values()))
