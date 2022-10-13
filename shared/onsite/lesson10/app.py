from flask import Flask

app = Flask(__name__)

@app.route("/")
def zobraz_pozdrav():
    return "<p>Ahoj, z desáté lekce!</p>" 
