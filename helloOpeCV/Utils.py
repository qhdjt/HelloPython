import cv2 as cv
from cv2.typing import MatLike


def namedShow(name: str, img: MatLike) -> None:
    if (name is None) or (img is None):
        raise ValueError("img cannot be None!")
    cv.namedWindow(name, cv.WINDOW_NORMAL)
    cv.imshow(name, img)
    cv.waitKey(0)

