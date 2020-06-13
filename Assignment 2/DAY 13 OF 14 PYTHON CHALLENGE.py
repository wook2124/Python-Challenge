from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs, save

"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

app = Flask("Remote Scrapper")

db = {}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search():
    jobs = []
    term = request.args.get("term").lower()

    if db.get(term):
        jobs.extend(db.get(term))
    else:
        jobs.extend(get_jobs(term))

        if len(jobs) == 0:
            return render_template("error.html", error_word=term, error_code=0)
        db[term] = jobs

    quantities = len(jobs)
    keyword = term.capitalize()
    return render_template("result.html", jobs=jobs, quantities=quantities, keyword=keyword)


@app.route("/download")
def download():
    keyword = request.args.get("keyword")

    if keyword is None:
        return render_template("error.html", error_word="", error_code=1)
    elif db.get(keyword.lower()) is None:
        return render_template("error.html", error_word="", error_code=1)

    keyword = keyword.lower()
    lists = db.get(keyword)
    save(lists)

    return send_file("jobs.csv", as_attachment=True, attachment_filename=f"{keyword}.csv")



app.run(host="0.0.0.0")
