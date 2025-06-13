import pytest
from img_masker import mask
from PIL import Image

TEST_WEB_URL = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/908.png"
TEST_IMG_URL = "tests/test_image.png"


def test_mask_transparency():
    """Test masking with transparent filter color."""
    img = mask(TEST_IMG_URL, filter_color="transparent")
    # Ensure function returns an Image object
    assert isinstance(img, Image.Image)


def test_mask_named_color():
    """Test masking with a named color."""
    img = mask(TEST_IMG_URL, filter_color="red")
    assert isinstance(img, Image.Image)


def test_mask_hex_color():
    """Test masking with a hex color."""
    img = mask(TEST_IMG_URL, filter_color="#FFFFFF")
    assert isinstance(img, Image.Image)


def test_mask_invalid_image():
    """Test handling of invalid image paths."""
    with pytest.raises(ValueError):  # Expect function to raise ValueError
        mask("invalid_file.png", filter_color="green")


def test_mask_web_url():
    """Test masking with a valid web URL."""
    img = mask(TEST_WEB_URL, filter_color="black")
    assert isinstance(img, Image.Image)
