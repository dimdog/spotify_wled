from PIL import Image
import requests
from io import BytesIO

def fetch_and_load_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    return image