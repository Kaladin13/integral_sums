import matplotlib.path as path


def get_path_from_dots(dots):
    return path.Path(dots)


def is_dot_inside(area, dot):
    return area.contains_point(dot)
