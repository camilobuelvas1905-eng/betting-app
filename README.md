from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_KEY = "29f7a951494a099822a42d50af2c51c1"

def implied_probability(odds):
    return 1 / odds

def model_probability():
    return 0.55  # modelo base simple

@app.route("/")
def home():
    return "API funcionando"

@app.route("/picks")
def picks():

    url = f"https://api.the-odds-api.com/v4/sports/soccer_epl/odds/?apiKey={API_KEY}&regions=eu&markets=h2h"

    data = requests.get(url).json()

    results = []

    for game in data[:5]:

        try:
            for bookmaker in game["bookmakers"]:
                for market in bookmaker["markets"]:
                    for outcome in market["outcomes"]:

                        odds = outcome["price"]

                        p_market = implied_probability(odds)
                        p_model = model_probability()

                        value = round(p_model - p_market, 3)

                        results.append({
                            "match": game["home_team"] + " vs " + game["away_team"],
                            "odds": odds,
                            "value": value
                        })

        except:
            continue

    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
