import csv

def save_file(jobs):
  file = open("jobs.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["title", "company", "location", "link", "salary"])
  for job in jobs:
    writer.writerow(list(job.values()))
  return