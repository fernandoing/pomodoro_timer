from flask import Flask, render_template, request, jsonify
from datetime import datetime, date
import json
import os

app = Flask(__name__)

DATA_FILE = "/data/stats.json"

# Default data structure
stats_data = {
    "history": [],
    "totals": {
        "pomodoros": 0,
        "skips": 0,
        "short_breaks": 0,
        "long_breaks": 0
    }
}

def load_stats():
    global stats_data
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                stats_data = json.load(f)
            except json.JSONDecodeError:
                pass  # use default if file corrupted

def save_stats():
    with open(DATA_FILE, "w") as f:
        json.dump(stats_data, f, indent=4)

def get_today_stats():
    today_str = str(date.today())
    for entry in stats_data["history"]:
        if entry["date"] == today_str:
            return entry
    # If not found, create it
    new_entry = {
        "date": today_str,
        "pomodoros": 0,
        "skips": 0,
        "short_breaks": 0,
        "long_breaks": 0
    }
    stats_data["history"].insert(0, new_entry)  # newest first
    return new_entry

@app.route("/")
def index():
    today_stats = get_today_stats()
    save_stats()
    return render_template("index.html", today_stats=today_stats, totals=stats_data["totals"], history=stats_data["history"])

@app.route("/update_stat", methods=["POST"])
def update_stat():
    data = request.json
    stat_type = data.get("type")
    today_stats = get_today_stats()
    if stat_type in today_stats:
        today_stats[stat_type] += 1
    if stat_type in stats_data["totals"]:
        stats_data["totals"][stat_type] += 1
    save_stats()
    return jsonify(success=True, today_stats=today_stats, totals=stats_data["totals"])

if __name__ == "__main__":
    load_stats()
    app.run(debug=True, host="0.0.0.0")
