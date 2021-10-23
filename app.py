from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv("./.env")

# SPOTIFY_CLIENTID = os.environ.get("SPOTIFY_CLIENTID")
# SPOTIFY_SECRET = os.environ.get("SPOTIFY_SECRET")
# print(SPOTIFY_CLIENTID, SPOTIFY_SECRET)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

