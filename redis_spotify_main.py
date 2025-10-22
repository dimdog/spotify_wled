import time
from lib.logging import logger
from lib.config import get_config
from lib.spotify import SpotifyClient, SpotifyError
from lib import constants
from lib.leds import turn_on_led, turn_off_led, blink_led
from lib.redis import redis_client


def main():
    config = get_config()
    spotify_client = SpotifyClient(config['spotify']['client_id'], config['spotify']['client_secret'], config['spotify']['redirect_uri'], config['spotify']['scope'])
    album_art_url = None
    old_album_art_url = None
    turn_on_led(constants.LEDs.spotify_url_grabber_on)
    while True:
        try:
            album_art_url = spotify_client.get_current_album_art_url()
            if album_art_url != old_album_art_url:
                redis_client.publish(constants.album_art_url_channel, album_art_url)
                old_album_art_url = album_art_url
                # flash led about change
                blink_led(constants.LEDs.spotify_url_changed)
                turn_off_led(constants.LEDs.spotify_url_error)
        except SpotifyError as e:
            turn_on_led(constants.LEDs.spotify_url_error)
            logger.error(f"Error getting current album art URL: {e}")

        time.sleep(1)


if __name__ == "__main__":
    main()