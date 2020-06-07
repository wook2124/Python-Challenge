from flask import Flask, render_template, request, redirect
from scrapper import aggregate_subreddits, check_subreddit
from remote import remote_jobs
from sof import get_jobs

"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

remote = remote_jobs()
sof = get_jobs()

jobs = remote_jobs() + get_jobs()


app = Flask("Remote World")

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]

@app.route("/")
def home():
  return render_template("home.html", subreddits=subreddits)


@app.route("/read")
def read():
  selected = []
  for subreddit in subreddits:
    if subreddit in request.args:
      selected.append(subreddit)
  posts = aggregate_subreddits(selected)
  posts.sort(key=lambda post: post['votes'], reverse=True)
  return render_template("read.html", selected=selected, posts=posts)


@app.route("/add",methods=['POST'])
def add():
  to_add = request.form.get('new-subreddit',None)
  if to_add:
    if "/" not in to_add:
      exists = check_subreddit(to_add)
      if exists:
        subreddits.append(to_add)
        return redirect("/")
      else:
        error = "That page does not exist."
    else:
      error = "Write the name without /r/"
  else:
    error = "Write a text."
  return render_template("add-failed.html", error=error)
    

app.run(host="0.0.0.0")