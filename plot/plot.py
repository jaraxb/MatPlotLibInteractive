import matplotlib.pyplot as plt
import numpy as np

__all__ = ["Plot", "PlotLine"]

class PlotLine:

    def __init__(self, x:np.ndarray, y:np.ndarray, label:str):
        self.x = x
        self.y = y
        self.label = label
        return

class Plot:

    def __init__(self):
        self.figure = plt.figure()
        self.axes:dict[int,plt.Axes] = {}
        self.axes[1] = self.figure.add_subplot(1,1,1)
        self.axes[1].set_title("Plot")
        self.axes[1].set_xlabel("X")
        self.axes[1].set_ylabel("Y")
        self.axes[1].legend()
        return

    def plot_data(self, plot_line:PlotLine, ax=1):
        self.axes[ax].plot(plot_line.x, plot_line.y, label=plot_line.label)
        return

    def update_plot(self, ax=1):
        self.axes[ax].relim()
        self.axes[ax].autoscale_view()
        self.axes[ax].legend_.legend_handles = [line.get_label() for line in self.axes[ax].lines]
        self.figure.canvas.draw()
        return