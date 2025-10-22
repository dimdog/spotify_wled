import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyError(Exception):
    pass

class SpotifyClient:
    
    def __init__(self, client_id, client_secret, redirect_uri, scope):
        self.client = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope
        ))
    
    def get_current_album_art_url(self):
        try:
            current_track = self.client.current_user_playing_track()
        except Exception as e:
            raise SpotifyError(f"Error getting current album art URL: {e}")

        if current_track and current_track['is_playing']:
            #track_name = current_track['item']['name']
            #artist = current_track['item']['artists'][0]['name']
            album_art_url = current_track['item']['album']['images'][0]['url']  # Largest image
            return album_art_url
        else:
            return None