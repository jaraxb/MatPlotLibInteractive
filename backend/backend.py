import tkinter as tk
import pandas as pd

from plot import Plot

__all__ = ["Backend"]

class Backend:

    def __init__(self):
        self.file_path = tk.StringVar(value="")
        self.file_data = pd.DataFrame()
        self.file_headers = tk.StringVar(value="")
        self.plot = Plot()
        return

    def load_file(self):
        self.file_data = pd.read_csv(self.file_path.get(), index_col=False)
        self.file_headers.set(",".join(sorted(self.file_data.columns)))
        return
