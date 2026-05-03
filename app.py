from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/picks")
def picks():

    matches = [
        "Barcelona vs Osasuna",
        "Arsenal vs Fulham",
        "Atalanta vs Genoa",
        "Real Madrid vs Sevilla"
    ]

    results = []

    for m in matches:
        results.append({
            "match": m,
            "value": round(random.uniform(0.05, 0.18), 2),
            "stake": round(random.uniform(10, 60), 2)
        })

    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
