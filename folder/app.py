from flask import Flask, render_template, jsonify, request
from proteins import get_sequences


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    query = request.json.get("query", "").strip()
    ids = query.replace(",", " ").split()
    seqs = get_sequences(ids)
    return jsonify(data=seqs)


if __name__ == "__main__":
    app.run(debug=True)
