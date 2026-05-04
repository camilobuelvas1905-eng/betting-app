import requests
from flask import Flask, jsonify

app = Flask(__name__)

API_KEY = "29f7a951494a099822a42d50af2c51c1"

@app.route("/")
def home():
    return "API funcionando"

@app.route("/picks")
def picks():

    url = f"https://api.the-odds-api.com/v4/sports/soccer_epl/odds/?apiKey={API_KEY}&regions=eu&markets=h2h"

    res = requests.get(url)
    data = res.json()

    picks = []

    for game in data[:5]:
        try:
            picks.append({
                "match": game["home_team"] + " vs " + game["away_team"],
                "value": 0.1,
                "stake": 25
            })
        except:
            continue

    return jsonify(picks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
