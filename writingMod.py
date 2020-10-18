import cv2
import numpy as np
# For image drawing
from PIL import Image, ImageDraw, ImageFont, ImageEnhance


def change_contrast(img, level):
    # Input is a Image type
    # use Image.fromarray() on numpy
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def contrast(c):
        return 128 + factor * (c - 128)
    return img.point(contrast)


def change_sharpness(img, level):
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(level)
    return img


def adjust(img, blevel, slevel, clevel, colevel):
    # brightness
    benhance = ImageEnhance.Brightness(img)
    img = benhance.enhance(blevel)
    # sharpness
    img = change_sharpness(img, slevel)
    # contrast
    img = change_contrast(img, clevel)
    # color
    cenhance = ImageEnhance.Color(img)
    img = cenhance.enhance(colevel)
    return img


def improveImage(img_dir):
    img = cv2.imread(img_dir, -1)
    rgb_planes = cv2.split(img)

    result_planes = []
    result_norm_planes = []
    for plane in rgb_planes:
        dilated_img = cv2.dilate(plane, np.ones((7,7), np.uint8))
        bg_img = cv2.medianBlur(dilated_img, 21)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        norm_img = cv2.normalize(diff_img, None, alpha=0, 
                                 beta=255, norm_type=cv2.NORM_MINMAX, 
                                 dtype=cv2.CV_8UC1)

        result_planes.append(diff_img)
        result_norm_planes.append(norm_img)

    result = cv2.merge(result_planes)
    result_norm = cv2.merge(result_norm_planes)
    return result_norm


def convert_image(image_dir):
    img = improveImage(image_dir)
    img = adjust(Image.fromarray(img), 
                  blevel=0.7, slevel=1, clevel=255, 
                  colevel=1)
    return img