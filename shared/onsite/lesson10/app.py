import csv

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("index.html", jmeno_stranky="DOMU")


@app.route("/clanky")
def topics():
    topics = read_topics("clanky.csv")
    return render_template(
        "topics.html",
        jmeno_stranky="CLANKY",
        clanky=topics
    )


def read_topics(jmeno_souboru: str) -> list:
    with open(jmeno_souboru, mode="r", encoding="utf-8") as csv_:
        reader = csv.DictReader(csv_)

        return [
            radek
            for radek in reader
        ]
