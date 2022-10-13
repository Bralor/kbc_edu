import csv

from flask import Flask, render_template, abort

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


@app.route("/clanky/<int:id>")
def topic_details(id):
    topics = read_topics("clanky.csv")

    for topic in topics:
        if topic["Id"] == str(id):
            result = topic         
            break

        else:
            result = None

    if not result:
        abort(404)

    return render_template(
        "topic.html",
        jmeno_stranky=f"CLANEK {id}",
        clanek=result
    )


def read_topics(jmeno_souboru: str) -> list:
    with open(jmeno_souboru, mode="r", encoding="utf-8") as csv_:
        reader = csv.DictReader(csv_)

        return [
            radek
            for radek in reader
        ]
