import tkinter as tk
from tkinter import Canvas

class ShapeSelectorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Shape Selector")
        
        self.canvas = Canvas(self.master, width=400, height=400, bg="white")
        self.canvas.pack()

        self.shapes = ["Rectangle", "Circle", "Triangle"]
        self.shape_sizes = {"Rectangle": (100, 100), "Circle": 100, "Triangle": 100}

        self.selected_shape = None
        
        self.create_buttons()
        self.create_shapes()

    def create_buttons(self):
        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack()

        for shape in self.shapes:
            button = tk.Button(self.buttons_frame, text=shape, command=lambda s=shape: self.display_shape(s))
            button.pack(side="left", padx=5, pady=5)

    def create_shapes(self):
        self.shapes_dict = {}

    def display_shape(self, shape):
        if self.selected_shape:
            self.canvas.delete(self.selected_shape)
        
        size = self.shape_sizes[shape]
        
        if shape == "Rectangle":
            self.selected_shape = self.canvas.create_rectangle(200 - size[0] // 2, 200 - size[1] // 2, 200 + size[0] // 2, 200 + size[1] // 2, fill="red", outline="")
        elif shape == "Circle":
            self.selected_shape = self.canvas.create_oval(200 - size // 2, 200 - size // 2, 200 + size // 2, 200 + size // 2, fill="green", outline="")
        elif shape == "Triangle":
            x0, y0 = 200, 200 - size // 2
            x1, y1 = 200 - size // 2, 200 + size // 2
            x2, y2 = 200 + size // 2, 200 + size // 2
            self.selected_shape = self.canvas.create_polygon(x0, y0, x1, y1, x2, y2, fill="blue", outline="")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeSelectorApp(root)
    root.mainloop()
