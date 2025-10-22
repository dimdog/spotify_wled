from enum import Enum

album_art_url_channel = "album_art_url"
panel_setter_enabled_key = "album_art_enabled"

#LEDs
class LEDs(Enum):
    spotify_url_grabber_on = "spotify_url_grabber_on"
    spotify_url_changed = "spotify_url_changed"
    spotify_url_error = "spotify_url_error"
    panel_setter_on = "panel_setter_on"
    panel_setter_changed = "panel_setter_changed"
    panel_setter_error = "panel_setter_error"