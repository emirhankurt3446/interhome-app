from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []

    if request.method == "POST":
        country = request.form.get("country")
        max_price = int(request.form.get("max_price") or 800)

        sample_data = [
            {"name": "Swiss Chalet A", "price": 650, "features": ["Park", "Balkon", "Mutfak"]},
            {"name": "Alpine Home B", "price": 720, "features": ["Park", "Mutfak"]},
            {"name": "Lake House C", "price": 800, "features": ["Park", "Balkon", "Çamaşır", "Mutfak"]},
        ]

        results = [r for r in sample_data if r["price"] <= max_price]
        results.sort(key=lambda x: x["price"])

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
