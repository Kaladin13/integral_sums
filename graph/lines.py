import tkinter as tk

from graph.canvas_values import get_graph_stats, revert_dot

root = tk.Tk()


canvas_w, canvas_h = get_graph_stats()
canvas = tk.Canvas(root, width=canvas_w, height=canvas_h)

dots = []
partition = tk.IntVar()


def get_area_dots():
    return [revert_dot(d) for d in dots]


def get_partition():
    return partition.get()


def close_win(event):
    root.destroy()


def init_screen():
    lb = tk.Label(text="""Use left click to draw lines and
    right click to close polyline""", font=("Arial", 15))
    lb.place(x=150, y=20)

    lb1 = tk.Label(root, text="Input partition", font=("Arial", 13))
    partition_slider = tk.Scale(root, from_=1, to=100, orient=tk.HORIZONTAL, variable=partition)

    lb1.pack()
    partition_slider.pack(pady=10)

    root.title("Draw G plot")


def bind_to_close():
    root.bind('<Key>', close_win)
    root.bind('<Button-1>', close_win)
    root.bind('<Button-3>', close_win)


def draw_to_start(event):
    if len(dots) >= 2:
        x_last, y_last = dots[-1]
        x0, y0 = dots[0]
        dots.append(dots[0])
        canvas.create_line(x_last, y_last, x0, y0)
        text = tk.Label(text="Press any key to continue...", font=("Arial", 14), borderwidth=2, relief="solid")
        text.place(x=30, y=550)
        bind_to_close()


def draw_line(event):
    x, y = event.x, event.y
    if x < 30 or y < 30:
        return

    if canvas.old_coords:
        x1, y1 = canvas.old_coords
        canvas.create_line(x, y, x1, y1)
    dots.append([x, y])
    canvas.old_coords = x, y


def start_graph_loop():
    canvas.pack()
    canvas.old_coords = None

    init_screen()

    root.bind('<Button-1>', draw_line)
    root.bind('<Button-3>', draw_to_start)
    root.mainloop()
