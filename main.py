from gui import RootWindow, InteractiveFrame, PlotCanvas

class App(RootWindow):

    def __init__(self):
        super().__init__()
        self.root.title("MatPlotLib Interactive")
        self.root.protocol("WM_DELETE_WINDOW", self.exit)

        self.interactive_frame = InteractiveFrame(self)
        self.plot_canvas = PlotCanvas(self)

    def __call__(self):
        self.interactive_frame()
        self.plot_canvas()

        super().__call__()

    def exit(self):
        self.root.quit()

if __name__ == "__main__":
    app = App()
    app()
