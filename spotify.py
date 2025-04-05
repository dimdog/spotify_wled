import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

with open("config.json", "r") as configfile:
    config = json.load(configfile)

CLIENT_ID = config['CLIENT_ID'] 
CLIENT_SECRET = config['CLIENT_SECRET'] 
REDIRECT_URI = config['CLIENT_SECRET'] 
SCOPE = config['SCOPE']

class SpotifyClient:
    
    def __init__(self):
        self.client = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope=SCOPE
        ))
    
    def get_current_album_art_url(self):
        current_track = self.client.current_user_playing_track()

        if current_track and current_track['is_playing']:
            track_name = current_track['item']['name']
            artist = current_track['item']['artists'][0]['name']
            album_art_url = current_track['item']['album']['images'][0]['url']  # Largest image
            return album_art_url
        else:
            return None

    def get_current_album_art_urls(self):
        current_track = self.client.current_user_playing_track()
        urls = []
        if current_track and current_track['is_playing']:
            track_name = current_track['item']['name']
            artist = current_track['item']['artists'][0]['name']
            for image in current_track['item']['album']['images']:
                urls.append(image['url'])
        return urls