import cv2
from PIL import Image


def change_picture(name, new_name):
    # show image before changes
    photo_pil_before = Image.open(name)
    photo_pil_before.show()
    # changes
    photo = cv2.imread(name)
    photo_hsv = cv2.cvtColor(photo, cv2.COLOR_BGR2HSV)
    cv2.imwrite(new_name, photo_hsv[:, :, 0])
    # show image after changes
    photo_pil_after = Image.open(new_name)
    photo_pil_after.show()