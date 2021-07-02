import cv2
import numpy as np


def change_photo(fname, directory_name):
    img = cv2.imread(fname)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h = hsv[:, :, 0]

    img[h >= 45] = (0, 0, 0)
    img[h <= 19] = (0, 0, 0)

    gray = np.copy(img[:, :, 0])

    thr, wb = cv2.threshold(gray, 3, 255, cv2.THRESH_BINARY)

    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(wb, 4, cv2.CV_32S)

    MAX_W = 70
    MAX_H = 70
    MIN_W = 20
    MIN_H = 20

    labels_to_add = []

    for i, stat in enumerate(stats):
        if stat[cv2.CC_STAT_WIDTH] > MAX_W or stat[cv2.CC_STAT_HEIGHT] > MAX_H:
            continue

        if stat[cv2.CC_STAT_WIDTH] < MIN_W or stat[cv2.CC_STAT_HEIGHT] < MIN_H:
            continue

        labels_to_add.append(i)
        print(f'Added {i}')

    wb[:, :] = 0

    for lbl in labels_to_add:
        print(f'Added {lbl}')
        wb[labels == lbl] = 255

    kernel = np.ones((5, 5), np.uint8)
    eroded = cv2.erode(wb, kernel, iterations=1)
    dilated = cv2.dilate(eroded, kernel, iterations=1)

    cv2.imwrite(directory_name, dilated)
    return directory_name
