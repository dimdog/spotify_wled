import time

from image_downloader import fetch_and_load_image
from spotify import SpotifyClient
from wled import send_image_to_wled
from wled_finder import scan_for_wled_servers 
try:
    print("Running... Press Ctrl+C to stop.")
    url = None
    spotify_client = SpotifyClient()
    wled_devices = scan_for_wled_servers() 
    panel_ip_address = None
    for device in wled_devices:
        if "panel" in device:
            panel_ip_address = wled_devices[device]
            break
    if not panel_ip_address:
        print("no panel found!")
    while True:
        # Your repeated task goes here
        album_art_url = spotify_client.get_current_album_art_url()
        if url != album_art_url:
            url = album_art_url
            image = fetch_and_load_image(url)
            send_image_to_wled(image, panel_ip_address)

        time.sleep(1)
except KeyboardInterrupt:
    print("\nKeyboardInterrupt received. Exiting.")





