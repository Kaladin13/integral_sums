from graph.canvas_values import get_graph_stats
from graph.lines import start_graph_loop, get_area_dots, get_partition
from utility.area import *
from utility.dispersion import get_func
from utility.dots import integral_sum
from utility.plot import add_rect_to_plot, draw_plot_from_path
from utility.rectangle import get_min_rectangle

global_rect = [(0, 0), (get_graph_stats()[0], get_graph_stats()[1])]


def get_custom_area():
    start_graph_loop()
    dots = get_area_dots()
    partition = get_partition()
    return dots, partition


def compute(dots, partition):
    area_path = get_path_from_dots(dots)
    rect = get_min_rectangle(dots)
    f = get_func()
    integral_sum(rect, area_path, partition, f)
    return area_path, rect


def plot(rect, area_path):
    add_rect_to_plot(rect)
    add_rect_to_plot(global_rect)
    draw_plot_from_path(area_path)


def main():
    dots, partition = get_custom_area()
    area_path, rect = compute(dots, partition)
    plot(rect, area_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
