import cv2
import os

trans_raw_dir = 'celeb_transparent/trans_raw/'
dst_dir = 'celeb_transparent/bokeh_bg_aligned/'

green_dir = 'celeb_transparent/green_bg_aligned/'


wild = cv2.imread('ccfam/backgrounds/bokeh.png')


def to_wild(img):
    for i in range(1024):
        for j in range(1024):
            if img[i][j][1] == 255:
                if img[i][j][0] == img[i][j][2] == 0:
                    img[i][j] = wild[i][j]
    return img


def to_green(img):
    alpha_channel = img[:, :, 3]
    alpha_channel = 255 - alpha_channel
    # alpha_channel = cv2.GaussianBlur(alpha_channel, (5, 5), 0)

    img = img[:, :, :3]
    img[:, :, 0] = cv2.add(img[:, :, 0], alpha_channel)  # B
    img[:, :, 1] = cv2.add(img[:, :, 1], alpha_channel)  # G
    img[:, :, 2] = cv2.add(img[:, :, 2], alpha_channel)  # R

    img[:, :, 0] = cv2.subtract(img[:, :, 0], alpha_channel)  # B
    img[:, :, 2] = cv2.subtract(img[:, :, 2], alpha_channel)  # R

    return img


# def to_blue(img):
#     alpha_channel = img[:, :, 3]
#     alpha_channel = 255 - alpha_channel
#     alpha_channel = cv2.GaussianBlur(alpha_channel, (5, 5), 0)
#
#     img = img[:, :, :3]
#     img[:, :, 0] = cv2.add(img[:, :, 0], alpha_channel)  # B
#     img[:, :, 1] = cv2.add(img[:, :, 1], alpha_channel)  # G
#     img[:, :, 2] = cv2.add(img[:, :, 2], alpha_channel)  # R
#
#     img[:, :, 1] = cv2.subtract(img[:, :, 1], alpha_channel)  # G
#     img[:, :, 2] = cv2.subtract(img[:, :, 2], alpha_channel)  # R
#
#     return img


def to_blue(img):
    alpha_channel = img[:, :, 3]
    alpha_channel = 255 - alpha_channel
    alpha_channel = cv2.GaussianBlur(alpha_channel, (5, 5), 0)

    img = img[:, :, :3]
    img[:, :, 0] = cv2.add(img[:, :, 0], alpha_channel)  # B
    img[:, :, 1] = cv2.add(img[:, :, 1], alpha_channel)  # G
    img[:, :, 2] = cv2.add(img[:, :, 2], alpha_channel)  # R

    alpha_channel_B = cv2.subtract(alpha_channel, 230)
    alpha_channel_G = cv2.subtract(alpha_channel, 170)
    alpha_channel_R = cv2.subtract(alpha_channel, 30)

    img[:, :, 0] = cv2.subtract(img[:, :, 0], alpha_channel_B)  # B
    img[:, :, 1] = cv2.subtract(img[:, :, 1], alpha_channel_G)  # G
    img[:, :, 2] = cv2.subtract(img[:, :, 2], alpha_channel_R)  # R

    return img


# def to_red(img):
#     alpha_channel = img[:, :, 3]
#     alpha_channel = 255 - alpha_channel
#     alpha_channel = cv2.GaussianBlur(alpha_channel, (5, 5), 0)
#
#     img = img[:, :, :3]
#     img[:, :, 0] = cv2.add(img[:, :, 0], alpha_channel)  # B
#     img[:, :, 1] = cv2.add(img[:, :, 1], alpha_channel)  # G
#     img[:, :, 2] = cv2.add(img[:, :, 2], alpha_channel)  # R
#
#     img[:, :, 0] = cv2.subtract(img[:, :, 0], alpha_channel)  # B
#     img[:, :, 1] = cv2.subtract(img[:, :, 1], alpha_channel)  # G
#
#     return img


def to_red(img):
    alpha_channel = img[:, :, 3]
    alpha_channel = 255 - alpha_channel
    # alpha_channel = cv2.GaussianBlur(alpha_channel, (5, 5), 0)

    img = img[:, :, :3]
    img[:, :, 0] = cv2.add(img[:, :, 0], alpha_channel)  # B
    img[:, :, 1] = cv2.add(img[:, :, 1], alpha_channel)  # G
    img[:, :, 2] = cv2.add(img[:, :, 2], alpha_channel)  # R

    alpha_channel_B = cv2.subtract(alpha_channel, 50)
    alpha_channel_G = cv2.subtract(alpha_channel, 10)
    alpha_channel_R = cv2.subtract(alpha_channel, 210)

    img[:, :, 0] = cv2.subtract(img[:, :, 0], alpha_channel_B)  # B
    img[:, :, 1] = cv2.subtract(img[:, :, 1], alpha_channel_G)  # G
    img[:, :, 2] = cv2.subtract(img[:, :, 2], alpha_channel_R)  # R

    return img


def to_white(img):
    alpha_channel = img[:, :, 3]
    alpha_channel = 255 - alpha_channel
    alpha_channel = cv2.GaussianBlur(alpha_channel, (5, 5), 0)

    img = img[:, :, :3]
    img[:, :, 0] = cv2.add(img[:, :, 0], alpha_channel)  # B
    img[:, :, 1] = cv2.add(img[:, :, 1], alpha_channel)  # G
    img[:, :, 2] = cv2.add(img[:, :, 2], alpha_channel)  # R

    return img


# alpha_channel = img[:, :, 3]
# alpha_channel = 255 - alpha_channel
# alpha_channel = cv2.GaussianBlur(alpha_channel, (5, 5), 0)

# _, mask = cv2.threshold(alpha_channel, 254, 255, cv2.THRESH_BINARY)  # binarize mask
# mask = 255 - mask
# mask = cv2.GaussianBlur(mask, (5, 5), 0)

# img = img[:, :, :3]
# img[:, :, 0] = img[:, :, 0] - alpha_channel  # B
# img[:, :, 1] = img[:, :, 1] - alpha_channel  # G
# img[:, :, 2] = img[:, :, 2] - alpha_channel  # R

# img[:, :, 0] = img[:, :, 0] - mask  # B
# img[:, :, 1] = img[:, :, 1] - mask  # G
# img[:, :, 2] = img[:, :, 2] - mask  # R

# img[:, :, 0] = cv2.GaussianBlur(img[:, :, 0], (5, 5), 0)  # B
# img[:, :, 1] = cv2.GaussianBlur(img[:, :, 1], (5, 5), 0)  # G
# img[:, :, 2] = cv2.GaussianBlur(img[:, :, 2], (5, 5), 0)  # R

# cnt = 0
# for img_name in os.listdir(trans_raw_dir):
#     print(cnt)
#     img = cv2.imread(os.path.join(trans_raw_dir, img_name), cv2.IMREAD_UNCHANGED)
#     img = to_green(img)
#     cv2.imwrite(os.path.join(dst_dir, str(cnt) + '_g.png'), img)
#     cnt += 1

cnt = 0
for img_name in os.listdir(green_dir):
    print(cnt)
    img = cv2.imread(os.path.join(green_dir, img_name), cv2.IMREAD_UNCHANGED)
    img = to_wild(img)
    cv2.imwrite(os.path.join(dst_dir, str(cnt) + '_k.png'), img)
    cnt += 1
