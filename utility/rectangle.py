import numpy as np


def get_rect_stats(rect):
    width = rect[1][0] - rect[0][0]
    height = rect[1][1] - rect[0][1]
    return width, height


def get_min_rectangle(dots):
    max_x, max_y = np.max(dots, axis=0)
    min_x, min_y = np.min(dots, axis=0)
    return [(min_x, min_y), (max_x, max_y)]

