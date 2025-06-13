# img-masker

A simple and lightweight Python tool for masking specific colors in images. Supports both local files and remote image URLs. Built on top of [Pillow](https://python-pillow.org/) for image processing.

## Features

- Mask (replace) pixels of a specific color or transparency in an image.
- Supports both local image files and remote image URLs.
- Customizable mask and background colors.

## Installation

You can install `img-masker` using pip:

```sh
pip install img-masker
```

## Requirements

- [Pillow](https://pypi.org/project/Pillow/)
- [requests](https://pypi.org/project/requests/)

## Usage

### Basic Example

```python
from img_masker import mask

# Mask all transparent pixels in an image with black, set background to white
masked_img = mask("https://example.com/image.png",)
masked_img.show()
```

### Parameters

- `image_url` (str): Path to a local image file or a remote image URL.
- `mask_color` (str): Color to use for masked pixels (default: `"black"`). Accepts any Pillow-compatible color string, e.g., `"red"`, `"#FF0000"`, `"transparent"`.
- `bg_color` (str): Color for non-masked pixels (default: `"white"`).
- `filter_color` (str): Target color to mask (default: `"transparent"`). Pixels matching this color will be replaced by `mask_color`.

### Masking a Specific Color

```python
# Mask all pure red pixels with blue, set background to white
masked_img = mask(
    "input.jpg",
    mask_color="blue",
    bg_color="white",
    filter_color="red"
)
masked_img.show()
```

### Masking Transparent Pixels

```python
# Mask all transparent pixels with black, keep others white
masked_img = mask(
    "input.png",
    mask_color="black", # Can also be remove since black is default mask_color
    bg_color="white", # Can also be remove since white is default bg_color
    filter_color="transparent" # Can also be remove since transparent is  default filter color
)
masked_img.save("masked.png")
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
