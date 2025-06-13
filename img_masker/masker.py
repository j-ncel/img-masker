from PIL import Image, ImageColor
import requests
from io import BytesIO
from functools import lru_cache
import os


@lru_cache(maxsize=10)
def fetch_image_bytes(image_url: str) -> bytes:
    """Fetches image bytes from a URL or local file, ensuring valid input."""
    if os.path.exists(image_url):
        with open(image_url, "rb") as f:
            return f.read()
    response = requests.get(image_url)
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch image from URL: {image_url}")
    return response.content


def filter_bool(item, filter_color, filter_rgba) -> bool:
    """Determines whether a pixel matches the filter color or is transparent."""
    return item[:3] == filter_rgba[:3] if filter_color != "transparent" else item[3] > 0


def mask(image_url: str, mask_color: str = "black", bg_color: str = "white", filter_color: str = "transparent") -> Image.Image:
    """Applies a masking to pixels matching a specific color in an image.
    Args:
        image_url (str): Local file path or URL of the image.
        mask_color (str): Color to replace matched pixels. Default is black.
        bg_color (str): Color for remaining pixels. Default is white.
        filter_color (str): Target color to apply masking. Default is transparent.

    Returns:
        Image.Image: A masked version of the image.
    """
    img_bytes = fetch_image_bytes(image_url)
    orig_image = Image.open(BytesIO(img_bytes)).convert("RGBA")
    masked_image = orig_image.copy()

    mask_rgba = ImageColor.getcolor(
        mask_color, "RGBA") if mask_color != "transparent" else (0, 0, 0, 0)
    bg_rgba = ImageColor.getcolor(
        bg_color, "RGBA") if bg_color != "transparent" else (0, 0, 0, 0)
    filter_rgba = ImageColor.getcolor(
        filter_color, "RGBA") if filter_color != "transparent" else (0, 0, 0, 0)

    new_data = [mask_rgba if filter_bool(
        item, filter_color, filter_rgba) else bg_rgba for item in masked_image.getdata()]

    masked_image.putdata(new_data)
    return masked_image
