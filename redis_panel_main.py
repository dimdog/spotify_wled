from lib.image_downloader import fetch_and_load_image
from wled import send_image_to_wled
from wled_finder import scan_for_wled_servers 
from lib.constants import album_art_url_key, panel_setter_enabled_key, LEDs
from lib.redis import redis_client
from lib.leds import turn_off_led, turn_on_led, blink_led

ENABLED = True
image = None

def get_panel_ip_address():
    wled_devices = scan_for_wled_servers() 
    for device in wled_devices:
        if "panel" in device:
            return wled_devices[device]
    return None

def get_subscribed_redis_client():
    pubsub = redis_client.pubsub()
    # Subscribe to the album art URL channel
    pubsub.subscribe(album_art_url_key)
    return pubsub

def check_panel_enabled():
    return redis_client.get(panel_setter_enabled_key) == "1"

def main():
    turn_off_led(LEDs.panel_setter_error)
    panel_ip_address = get_panel_ip_address()
    if not panel_ip_address:
        turn_on_led(LEDs.panel_setter_error)
        print("No panel found!")
        exit(1)

    redis_client = get_subscribed_redis_client()
    turn_on_led(LEDs.panel_setter_on)
    for message in redis_client.listen():
        if message['type'] == 'message':
            album_art_url = message['data']
            if album_art_url and ENABLED:
                image = fetch_and_load_image(album_art_url)
                send_image_to_wled(image, panel_ip_address)
                blink_led(LEDs.panel_setter_changed)

if __name__ == "__main__":
    main()





