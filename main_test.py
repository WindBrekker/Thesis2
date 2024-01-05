import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from matplotlib import cm

class HeatmapWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Heatmap Reader")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.canvas = HeatmapCanvas()
        layout.addWidget(self.canvas)

        self.statusBar().showMessage("Hover over the heatmap to read values.")

        self.canvas.mpl_connect('motion_notify_event', self.on_hover)

    def on_hover(self, event):
        if event.inaxes:
            x, y = event.xdata, event.ydata
            value = self.canvas.get_value_at(x, y)
            self.statusBar().showMessage(f"Hovering at ({x:.2f}, {y:.2f}), Value: {value:.2f}")

class HeatmapCanvas(FigureCanvas):
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
        self.compute_initial_figure()

    def compute_initial_figure(self):
        # Replace this with your heatmap data
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        cmap = cm.get_cmap("viridis")

        self.img = self.ax.imshow(data, cmap=cmap, origin='lower', interpolation='nearest')
        self.fig.colorbar(self.img, ax=self.ax)

    def get_value_at(self, x, y):
        # Interpolate to get the value at the specified coordinates
        value = self.img.get_array()[int(y + 0.5), int(x + 0.5)]
        return value

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HeatmapWindow()
    window.show()
    sys.exit(app.exec())
