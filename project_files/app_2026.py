import os
import sqlite3
from flask import Flask, render_template, g

app = Flask(__name__)
app.config["DATABASE"] = os.path.join(os.path.dirname(__file__), "MyDB.db")

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
        print("Connected to the database")
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()

@app.route("/")
def home():
    return render_template("index.html", title="Home Page")

@app.route("/about")
def about():
    return render_template("about.html", title="About Page")

if __name__ == "__main__":
    app.run(debug=True)
