import pandas as pd
from flask import Flask
import time
import json

# creating api with flask
app = Flask(__name__)


# creating routes for the query functions
@app.route("/keepalive")
def get_keep_alive():
    return keep_alive()


@app.route("/userStats/<user_id>")
def get_user_stats(user_id):
    return json.dumps(user_stats(user_id))


@app.route("/sessionId/<session_id>")
def get_session_data(session_id):
    return json.dumps(session(session_id))


# creating headers for the csv files
requests = pd.read_csv("requests.csv", sep=',', names=["timestamp", "session_id", "partner", "user_id", "bid", "win"])
clicks = pd.read_csv("clicks.csv", sep=',', names=["timestamp", "session_id", "time"])
impressions = pd.read_csv("impressions.csv", sep=",", names=["timestamp", "session_id", "duration"])


# checking if the csv files have problems
def keep_alive():
    if requests.empty or clicks.empty or impressions.empty:
        return "detected a problem"
    else:
        return "service is up and ready to go"


# extracting user stats
def user_stats(user_id):
    data = requests[requests["user_id"] == user_id]  # extracting only relevant data
    num_impression = impressions[impressions["session_id"].isin(data["session_id"])]
    num_clicks = clicks[clicks["session_id"].isin(data["session_id"])]
    avg_price = data["bid"][data["win"] == True].mean()
    mean = num_impression["duration"].median()
    max_time = num_clicks["time"].max()
    # creating a dict to later return it in a json formant
    data_dict = {
        "num_of_requests": int(data.shape[0]),
        "num_of_impressions": int(num_impression.shape[0]),
        "num_of_clicks": int(num_clicks.shape[0]),
        "avg_price": float(avg_price),
        "median_impressions": float(mean),
        "max_time_til_clicks": float(max_time)
    }

    return data_dict


def session(session_id):
    data = requests[requests["session_id"] == session_id]  # extracting only relevant data
    begin = int(time.time())  # session start time
    finish = data["timestamp"].max()
    name = data["partner"].iloc[0]
    # creating a dict to later return it in a json formant
    data_dict = {
        "timestamp": begin,
        "latest timestamp": int(finish),
        "partner name": str(name)
    }
    return data_dict


# for testing functions
print(keep_alive())
print(user_stats("efb64b4e-3655-4a4a-af2d-4d62945eb6d0"))
print(session("27820661-9082-4c93-8961-336423fc46c9"))
