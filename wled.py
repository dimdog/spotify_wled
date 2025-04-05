import requests
import numpy as np
from PIL import Image
import time
# WLED Configuration
WLED_IP = "192.168.86.50"  # Replace with your WLED device IP
GRID_WIDTH = 22
GRID_HEIGHT = 27

# Load and process image

def convert_image_to_led_array(image):
    leds = []
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            r, g, b, *a = image.getpixel((x, y))
            leds.append([r,g,b])
    return leds

def split_send_leds(led_array, ip_address):
    step = 200
    for start_led in range(0, len(led_array), step):
        print(start_led)
        start = [start_led]
        data = led_array[start_led:start_led+step]
        start.extend(data)
        data = {
            "bri": '200',
            "live": True,
            "seg": [
                { "i": start}
            ],
        }
        WLED_JSON_URL = f"http://{ip_address}/json/state"
        response = requests.post(WLED_JSON_URL, json=data)
        if response.status_code == 200:
            print(response.json())
            print("Image sent successfully!")
        else:
            print("Failed to send image:", response.text)

def send_image_to_wled(image, ip_address=WLED_IP):
    resized = image.resize((GRID_WIDTH, GRID_HEIGHT))  # Resize for LED matrix
    led_array = convert_image_to_led_array(resized)
    split_send_leds(led_array, ip_address)
    time.sleep(.5)
    split_send_leds(led_array, ip_address)

if __name__ == "__main__": 
    #image = Image.open("images/red_square.jpg")  # Resize for LED matrix
    #image = Image.open("images/test.png")  # Resize for LED matrix
    image = Image.open("images/simple_flag.png")  # Resize for LED matrix

    send_image_to_wled(image)