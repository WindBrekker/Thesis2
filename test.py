import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class ListNavigator(QWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.current_index = 0
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.label = QLabel(self.data[self.current_index], self)
        layout.addWidget(self.label)

        next_button = QPushButton("Next", self)
        prev_button = QPushButton("Previous", self)
        next_button.clicked.connect(self.next_item)
        prev_button.clicked.connect(self.previous_item)

        layout.addWidget(next_button)
        layout.addWidget(prev_button)

        self.setLayout(layout)

    def next_item(self):
        if self.current_index < len(self.data) - 1:
            self.current_index += 1
            self.label.setText(self.data[self.current_index])

    def previous_item(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.label.setText(self.data[self.current_index])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    data = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
    window = ListNavigator(data)
    window.setWindowTitle("List Navigator")
    window.setGeometry(100, 100, 300, 150)
    window.show()
    app.exec()
