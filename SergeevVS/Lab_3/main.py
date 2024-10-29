import sys
import window
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QSlider, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtCore import Qt
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = window.ImageCompressor()
    window.show()
    sys.exit(app.exec_())

