import tkinter as tk
from tkinter import ttk,filedialog

from . import RootWindow, MainFrame, SubFrame
from plot import PlotLine

__all__ = ["InteractiveFrame", "FileFrame", "DataFrame"]

class InteractiveFrame(MainFrame):

    def __init__(self, parent:RootWindow):
        super().__init__(parent)

        self.file_frame = FileFrame(self)
        self.data_frame = DataFrame(self)
        return

    def __call__(self):
        super().__call__(side=tk.TOP, fill=tk.X)

        self.file_frame()
        self.data_frame()
        return

class FileFrame(SubFrame):

    frame_text = "Load File"
    file_extentsions = [
        ("CSV files", "*.csv"),
        ("All files", "*.*"),
    ]

    def __init__(self, parent:InteractiveFrame):
        super().__init__(parent)
        self.file_path = self.backend.file_path

        # load button
        self.load_button = tk.Button(self.master_frame, text="Select", command=self.select_file)

        # file path label
        self.path_label = tk.Label(self.master_frame, text="No file selected", state="disabled")
        self.file_path.trace_add("write",self.set_label)
        return

    def __call__(self):
        super().__call__(side=tk.LEFT, fill=tk.X)

        self.load_button.pack(side=tk.LEFT)
        self.path_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        return

    def select_file(self):
        file_path = filedialog.askopenfilename(title="Select Files", filetypes=self.file_extentsions, initialdir="input_data")
        if not file_path:
            self.file_path.set("")
            return
        self.file_path.set(file_path)

        self.backend.load_file()
        return

    def set_label(self, *args):
        file_path = self.file_path.get()
        if not file_path:
            file_path = "No file selected"

        self.path_label.config(state="normal")
        self.path_label.config(text=file_path)
        self.path_label.config(state="disabled")
        return

class DataFrame(SubFrame):

    frame_text = "Select Data"

    def __init__(self, parent:InteractiveFrame):
        super().__init__(parent)
        self.file_data = self.backend.file_data
        self.file_headers = self.backend.file_headers

        # axis comboboxes
        self.axis_comboboxes = {
            "x": ttk.Combobox(self.master_frame, state="normal"),
            "y": ttk.Combobox(self.master_frame, state="normal"),
        }
        self.file_headers.trace_add( "write", self.set_combobox_values)
        for axis in self.axis_comboboxes:
            self.axis_comboboxes[axis].bind("<KeyRelease>", lambda event, ax=axis: self.filter_columns(ax))

        self.plot_button = tk.Button(self.master_frame, text="Plot", command=self.plot_data)
        return

    def __call__(self):
        super().__call__(side=tk.LEFT, fill=tk.X)

        for ax in self.axis_comboboxes:
            self.axis_comboboxes[ax].pack()
        self.plot_button.pack()
        return

    def set_combobox_values(self, *args):
        headers = self.file_headers.get().split(",")
        for axis in self.axis_comboboxes:
            self.axis_comboboxes[axis].config(values=["", *sorted(headers)])
            self.axis_comboboxes[axis].set("")
        return

    def filter_columns(self, axis:str):
        input_value = self.axis_comboboxes[axis].get()
        current_columns = list(self.axis_comboboxes[axis]["values"])
        new_columns = [col for col in current_columns if input_value.lower() in col.lower()]
        self.axis_comboboxes[axis]["values"] = ["", *sorted(new_columns)]
        return

    def plot_data(self, ax=1):
        headers = {axis:self.axis_comboboxes[axis].get() for axis in self.axis_comboboxes}
        if any([headers[key] not in self.file_data.columns for key in headers]): return

        plot_line = PlotLine(
            **{self.file_data[headers[axis]].to_numpy() for axis in headers},
            label=f"{headers[0]} vs {headers[1]}"
        )

        self.backend.plot.plot_data(plot_line=plot_line, ax=ax)
        self.backend.plot.update_plot(ax=ax)
        self.parent.parent.plot_canvas.update_canvas()
        return
