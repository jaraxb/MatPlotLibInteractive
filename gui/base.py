import tkinter as tk

from backend import Backend

__all__ = ["RootWindow", "MainFrame", "SubFrame"]

class RootWindow:

    def __init__(self):
        self.root = tk.Tk()
        self.master = self.root
        self.backend = Backend()
        return

    def __call__(self):
        self.root.mainloop()
        return

class MainFrame:

    def __init__(self, parent:RootWindow):
        self.parent = parent
        self.master = parent.root
        self.backend = parent.backend

        self.master_frame = tk.Frame(self.master)
        return

    def __call__(self, side=tk.TOP, fill=tk.BOTH, expand=False):
        self.master_frame.pack(side=side, fill=fill, expand=expand)
        return

class SubFrame:

    frame_text = ""

    def __init__(self, parent:MainFrame):
        self.parent = parent
        self.master = parent.master_frame
        self.backend = parent.backend

        self.master_frame = tk.LabelFrame(self.master, text=self.frame_text)
        return

    def __call__(self, side=tk.TOP, fill=tk.BOTH, expand=False):
        self.master_frame.pack(side=side, fill=fill, expand=expand)
        return
