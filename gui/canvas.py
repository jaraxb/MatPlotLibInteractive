
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from . import RootWindow, MainFrame

__all__ = ["PlotCanvas"]

class PlotCanvas(MainFrame):

    def __init__(self, parent:RootWindow):
        super().__init__(parent)
        self.plot = self.backend.plot

        self.canvas = FigureCanvasTkAgg(self.plot.figure, master=self.parent.root)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.parent.root)
        return

    def __call__(self):
        super().__call__(expand=True)

        self.canvas.get_tk_widget().pack()
        self.toolbar.pack()
        return

    def update_canvas(self):
        self.canvas.draw()
        self.toolbar.update()
        return
