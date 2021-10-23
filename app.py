from flask import Flask
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
load_dotenv("./.env")

SPOTIFY_CLIENTID = os.environ.get("SPOTIFY_CLIENTID")
SPOTIFY_SECRET = os.environ.get("SPOTIFY_SECRET")
# print(SPOTIFY_CLIENTID, SPOTIFY_SECRET)

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENTID,
                                                           client_secret=SPOTIFY_SECRET))


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENTID,
                                               client_secret=SPOTIFY_SECRET,
                                               redirect_uri="https://localhost.com",
                                               scope="user-library-read"))

# results = sp.search(q='weezer', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])

data = sp.current_user_playing_track()
print(data)