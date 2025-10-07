from flask import Flask, render_template, request
import pandas as pd
from src.team_builder import build_teams

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        teams = build_teams("data/students.csv", n_teams=3)
        return render_template("teams.html", tables=teams.to_html(classes='table table-striped'))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
