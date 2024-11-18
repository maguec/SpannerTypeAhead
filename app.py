#!/usr/bin/env python

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from google.cloud import spanner
import json
from collections import namedtuple
from datetime import datetime

app = Flask(
    __name__,
    static_url_path="/docs",
    static_folder="docs",
)

bootstrap = Bootstrap()
s = spanner.Client()
instance = s.instance("typeahead")
client = instance.database("typeaheaddb")

def station_data(name):
    query = "SELECT * FROM Station WHERE name = \"{}\"".format(name)
    with client.snapshot() as snapshot:
        results = snapshot.execute_sql(query)
        for r in results:
            return(r)


def fts(name):
    suggest = []
    query = "SELECT name FROM Station WHERE SEARCH_NGRAMS(name_Tokens,'{}')".format(name)
    with client.snapshot() as snapshot:
        results = snapshot.execute_sql(query)
        for r in results:
            suggest.append(r[0])

    return(suggest)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/display', methods = ['POST'])
def display():
   f = request.form
   info = station_data(f['station'])
   return render_template('results.html', result = info)

@app.route("/autocomplete")
def autocomplete():
    name = request.args.get('term')
    suggest = fts(name)
    return(
        json.dumps(
            [{'value': item,
              'label': item,
              'id': item,
              'score': 1}for item in suggest]))

if __name__ == "__main__":
    bootstrap.init_app(app)
    app.debug = True
    app.run(port=5000, host="0.0.0.0")
