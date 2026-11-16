from flask import Flask, render_template
from data import certifications

app = Flask(__name__)

@app.route("/")
def home():

    total_progress = round(
        sum(c['progress'] for c in certifications) /
        len(certifications)
    )

    total_cost = sum(c['price_brl'] for c in certifications)

    saved = 630

    remaining = total_cost - saved

    return render_template(
        "index.html",
        certifications=certifications,
        total_progress=total_progress,
        total_cost=total_cost,
        saved=saved,
        remaining=remaining
    )


if __name__ == "__main__":
    app.run(debug=True)