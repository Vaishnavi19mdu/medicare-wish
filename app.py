from flask import Flask, render_template, request
from analyzer import analyze_report

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    if request.method == "POST":
        report = {
            "Hemoglobin": {"value": float(request.form["hb"]), "low": 12, "high": 16},
            "Glucose": {"value": float(request.form["glucose"]), "low": 70, "high": 140}
        }
        results = analyze_report(report)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
