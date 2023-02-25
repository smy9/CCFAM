import cv2
import numpy as np


def replace_bg(image, bg, mask):
    image = image * (mask / 255)
    bg = bg * ((255 - mask) / 255)

    return cv2.addWeighted(image, 1, bg, 0.98, 0)


def blue_bg():
    blue = np.ones((1024, 1024, 3))

    blue[:, :, 0] = blue[:, :, 0] * 200
    blue[:, :, 1] = blue[:, :, 1] * 130
    blue[:, :, 2] = blue[:, :, 2] * 2

    return blue


def red_bg():
    red = np.ones((1024, 1024, 3))

    red[:, :, 0] = red[:, :, 0] * 50
    red[:, :, 1] = red[:, :, 1] * 10
    red[:, :, 2] = red[:, :, 2] * 210

    return red


def white_bg():
    white = np.ones((1024, 1024, 3)) * 255

    return white


def blur_bg(img):
    return cv2.GaussianBlur(img, (999, 999), 0)


if __name__ == "__main__":
    image = cv2.imread('image path')
    mask = cv2.imread('mask path')
    cv2.imwrite('result.png', replace_bg(image, blue_bg(), mask))
