import sqlite3
import os
from flask import Flask, jsonify, redirect, request, g, abort
from pubnub import Pubnub

app = Flask(__name__)
app.config['DEBUG'] = True

USER_NAME = ""
CHANNEL = "GitTreats"

pubnub = Pubnub(
    publish_key=os.environ["PUBNUB_GT_PUBLISH"],
    subscribe_key=os.environ["PUBNUB_GT_SUBSCRIBE"])


@app.route('/', methods=['POST'])
def add_treat():
    if not request.json:
        abort(400)
    json = request.json
    action = json["action"]
    user_name = json["pull_request"]["user"]["login"]
    merged = json["pull_request"]["merged"]
    if action == "closed" and user_name == USER_NAME and merged:
        pubnub.publish(channel=CHANNEL, message="Give \'em a treat")
        return jsonify(info="Sweets Dispensed")
    return jsonify(info="OK")


if __name__ == '__main__':
    app.run()
