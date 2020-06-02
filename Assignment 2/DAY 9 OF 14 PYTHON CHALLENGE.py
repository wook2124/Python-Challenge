import requests
from flask import Flask, render_template, request


base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories. 
# /?order_by=new
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories 
# /?order_by=popular
popular = f"{base_url}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
  return f"{base_url}/items/{id}"

db = {}
app = Flask("DayNine")

@app.route("/")
def home():
  # The template should reflect the current order_by selection.
  order_by = request.args.get('order_by', 'popular')
  if order_by not in db:
    print("Requesting")
    if order_by == 'popular':
      news = requests.get(popular)
    elif order_by == 'new':
      news = requests.get(new)
    results = news.json()['hits']
    db[order_by] = results
  results = db[order_by]
  return render_template("index.html", order_by=order_by, results = results)

# /<id>
@app.route("/<id>")
def detail(id):
  detail_request = requests.get(make_detail_url(id))
  result = detail_request.json()
  return render_template("detail.html", result = result)

app.run(host="0.0.0.0")