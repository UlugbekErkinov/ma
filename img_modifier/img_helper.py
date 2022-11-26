from PIL import Image, ImageEnhance
import logging

import img_modifier.color_filter as cf

logger = logging.getLogger()

# constants
CONTRAST_FACTOR_MAX = 1.5
CONTRAST_FACTOR_MIN = 0.5

SHARPNESS_FACTOR_MAX = 3
SHARPNESS_FACTOR_MIN = -1

BRIGHTNESS_FACTOR_MAX = 1.5
BRIGHTNESS_FACTOR_MIN = 0.5


def get_img(path):
    """Return PIL.Image object"""

    if path == "":
        logger.error("path is empty of has bad format")
        raise ValueError("path is empty of has bad format")

    try:
        return Image.open(path)
    except Exception:
        logger.error(f"can't open the file {path}")
        raise ValueError(f"can't open the file {path}")


def resize(img, width, height):
    """Resize image"""

    return img.resize((width, height))


def rotate(img, angle):
    """Rotate image"""

    return img.rotate(angle, expand=True)


def color_filter(img, filter_name):
    return cf.color_filter(img, filter_name)


def brightness(img, factor):
    if factor > BRIGHTNESS_FACTOR_MAX or factor < BRIGHTNESS_FACTOR_MIN:
        raise ValueError("factor should be [0-2]")

    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(factor)


def contrast(img, factor):
    if factor > CONTRAST_FACTOR_MAX or factor < CONTRAST_FACTOR_MIN:
        raise ValueError("factor should be [0.5-1.5]")

    enhancer = ImageEnhance.Contrast(img)
    return enhancer.enhance(factor)


def sharpness(img, factor):
    if factor > SHARPNESS_FACTOR_MAX or factor < SHARPNESS_FACTOR_MIN:
        raise ValueError("factor should be [0.5-1.5]")

    enhancer = ImageEnhance.Sharpness(img)
    return enhancer.enhance(factor)


def flip_left(img):
    return img.transpose(Image.FLIP_LEFT_RIGHT)


def flip_top(img):
    return img.transpose(Image.FLIP_TOP_BOTTOM)


def save(img, path):
    img.save(path)


def open_img(img):
    img.open()
