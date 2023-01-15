import matplotlib.pyplot as plt
import matplotlib.patches as patches

from utility.rectangle import get_rect_stats

fig, ax = plt.subplots()


def add_rect_to_plot(rect):
    width, height = get_rect_stats(rect)
    ax.add_patch(patches.Rectangle(rect[0], width, height, fill=False, edgecolor='red'))


def add_legend(int_sum, disp):
    black_patch = patches.Patch(color='black', label="Computed integral sum: {:.3f}".format(int_sum))
    red_patch = patches.Patch(color='red', label="Computed dispersion: {:.3f}".format(disp))
    ax.legend(handles=[black_patch, red_patch], loc='lower left', bbox_to_anchor=(0, 1))


def add_dot_to_plot(x, y, colour="blue"):
    plt.plot([x], [y], marker="o", markersize=1, markerfacecolor=colour, markeredgecolor=colour)


def draw_plot_from_path(area_path):
    patch = patches.PathPatch(area_path, facecolor='yellow', lw=2)
    ax.add_patch(patch)
    ax.axis('scaled')
    plt.show()
