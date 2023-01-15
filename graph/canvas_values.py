WIDTH = 600
HEIGHT = 600


def get_graph_stats():
    return WIDTH, HEIGHT


def revert_dot(dot):
    return [dot[0], HEIGHT - dot[1]]
