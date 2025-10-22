from gpiozero import LED, BadPinFactory#, Button
from lib.constants import LEDs
from lib.logging import logger

try:
    led_map = {
        LEDs.spotify_url_grabber_on: LED(17),
        LEDs.spotify_url_changed: LED(27),
        LEDs.spotify_url_error: LED(22),
        LEDs.panel_setter_on: LED(23),
        LEDs.panel_setter_changed: LED(24),
        LEDs.panel_setter_error: LED(25),
        # panel_setter_enabled: LED(26), TODO
    }
except BadPinFactory as e:
    logger.error(f"Error initializing LEDs: {e}")
    led_map = None

def turn_on_led(led_name: LEDs):
    if led_map:
        led_map[led_name.value].on()

def turn_off_led(led_name: LEDs):
    if led_map:
        led_map[led_name.value].off()

def blink_led(led_name: LEDs, duration=1):
    if led_map:
        led_map[led_name.value].blink(duration)