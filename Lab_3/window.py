import os
import pathlib
import sys

from PIL.ImageQt import ImageQt
from qtpy import uic

import MGK
import numpy as np
import cv2
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QSlider, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage

# типы переменным и многопоточность, лэйблу size добавить коэфицент сжатия
class ImageCompressor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.path = pathlib.Path.cwd()
        uic.loadUi(self.path / r"ff.ui", self)
        self.file_Path:str = None
        self.compressed_image = None

        # UI elements
        self.label = self.findChild(QLabel, "labels")
        self.size = self.findChild(QLabel, "size")
        self.sliderR = self.findChild(QSlider, "sliderR")
        self.sliderR.setMinimum(1)
        self.sliderR.setMaximum(100)
        self.sliderR.setValue(100)
        self.sliderR.valueChanged.connect(self.update_image)

        self.sliderG = self.findChild(QSlider, "sliderG")
        self.sliderG.setMinimum(1)
        self.sliderG.setMaximum(100)
        self.sliderG.setValue(100)
        self.sliderG.valueChanged.connect(self.update_image)

        self.sliderB = self.findChild(QSlider, "sliderB")
        self.sliderB.setMinimum(1)
        self.sliderB.setMaximum(100)
        self.sliderB.setValue(100)
        self.sliderB.valueChanged.connect(self.update_image)

        self.load_button = self.findChild(QPushButton, "load_button")
        self.load_button.clicked.connect(self.load_image)

        self.save_button = self.findChild(QPushButton, "save_button")
        self.save_button.clicked.connect(self.save_image)
        self.save_button.setEnabled(False)


    def load_image(self):
        options = QFileDialog.Options()
        self.file_Path, _ = QFileDialog.getOpenFileName(self, "Load Image", "", "Image Files (*.png *.jpg *.bmp)",
                                                        options=options)
        self.file_extension = os.path.splitext(self.file_Path)[1]
        self.Temp_size = os.path.getsize(self.file_Path)
        print(self.file_Path)
        if self.file_Path:
            self.update_image()

    def update_image(self):
        if self.file_Path is None:
            print("Non name")
            return
        compression_factor = [self.sliderR.value(), self.sliderG.value(), self.sliderB.value()]
        self.compressed_image = MGK.compress_image_pca(self.file_Path, compression_factor)
        self.compressed_image.save(os.getcwd() +"/temp"+self.file_extension)
        file_size = os.path.getsize(os.getcwd()+"/temp"+self.file_extension)/self.Temp_size
        self.size.setText(str(round(file_size, 1)))
        self.show_image(self.compressed_image)
        self.save_button.setEnabled(True)

    def show_image(self, image):
        # Конвертирование изображения из BGR в RGB
        pixmap = QPixmap.fromImage(ImageQt(image))
        self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.KeepAspectRatio))

    def save_image(self):
        if self.compressed_image is not None:
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                       options=options)
            if file_name:
                print(file_name)
                self.compressed_image.save(file_name+self.file_extension)


# Запуск приложения
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageCompressor()
    window.show()
    sys.exit(app.exec_())
