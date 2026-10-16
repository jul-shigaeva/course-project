from flask import Flask, render_template, jsonify, request
from proteins import get_sequences
from table import get_table


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

@app.route("/table", methods=["POST"])
def table_route():
    query = request.json.get("query", "").strip()
    ids = query.replace(",", " ").upper().split()
    if not ids:
        return jsonify(error="Введите COG ID"), 400
    try:
        rows = get_table(ids)
    except Exception as e:
        return jsonify(error=f"Ошибка получения данных: {e}"), 500
    return jsonify(table=rows)


if __name__ == "__main__":
    app.run(debug=True)
