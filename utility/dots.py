from collections import namedtuple

from utility.area import is_dot_inside
from utility.dispersion import add_diff_dot, get_dispersion
from utility.plot import add_dot_to_plot, add_legend
from utility.rectangle import get_rect_stats

dot = namedtuple("dot", ["x", "y"])


def integral_sum(rect, area, n, f):
    width, height = get_rect_stats(rect)

    x_space = width / (2 * n)
    y_space = height / (2 * n)

    high_point = [rect[0][0], rect[1][1]]
    computed_res = 0
    area_sq = x_space * y_space * 4

    for i in range(n):
        for j in range(n):
            x_offset = high_point[0] + x_space * (1 + 2 * i)
            y_offset = high_point[1] - y_space * (1 + 2 * j)

            if is_dot_inside(area, (x_offset, y_offset)):
                # compute integral sum
                computed_res += f(x_offset, y_offset)

                # add dot to dispersion
                add_diff_dot(x_offset, y_offset)

                add_dot_to_plot(x_offset, y_offset, "red")
            else:
                add_dot_to_plot(x_offset, y_offset)

    integral_s = computed_res * area_sq
    dispersion = get_dispersion(area_sq, x_space * 2)

    if integral_s == 0:
        print("Error when computing integral sum, quitting")
        exit(1)

    add_legend(integral_s, dispersion)

