import os
import pathlib
from PIL.ImageQt import ImageQt
from qtpy import uic
import MGK
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QSlider, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class ImageCompressor:
    def __init__(self):
        self.file_path = None
        self.temp_size = None
        self.compressed_image = None

    def load_image(self, file_path):
        self.file_path = file_path
        self.temp_size = os.path.getsize(self.file_path)

    def get_size_img(self, value):
        from PIL import Image
        im = Image.open(self.file_path)
        size_img = min(im.size)
        return int(value / 100 * size_img)

    def compress_image(self, compression_factors):
        self.compressed_image = MGK.compress_image_pca(self.file_path, compression_factors)
        return self.compressed_image

    def get_file_size_ratio(self):
        compressed_size = os.path.getsize(os.getcwd() + "/temp" + os.path.splitext(self.file_path)[1])
        return compressed_size / self.temp_size

    def get_size_difference_percentage(self):
        compressed_size = os.path.getsize(os.getcwd() + "/temp" + os.path.splitext(self.file_path)[1])
        return ((self.temp_size - compressed_size) / self.temp_size) * 100


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.path = pathlib.Path.cwd()
        uic.loadUi(self.path / r"SergeevVS/Lab_3/veiw.ui", self)

        # Создаем экземпляр ImageCompressor
        self.image_compressor = ImageCompressor()
        # UI elements
        self.label = self.findChild(QLabel, "labels")
        self.size = self.findChild(QLabel, "size")
        self.proc_compress = self.findChild(QLabel, "size_2")
        self.size_difference = self.findChild(QLabel, "size_difference")  # Новый QLabel для отображения разницы
        self.sliderR = self.findChild(QSlider, "sliderR")
        self.sliderG = self.findChild(QSlider, "sliderG")
        self.sliderB = self.findChild(QSlider, "sliderB")
        self.load_button = self.findChild(QPushButton, "load_button")
        self.save_button = self.findChild(QPushButton, "save_button")

        self.setup_ui()

    def setup_ui(self):
        self.sliderR.setMinimum(0)
        self.sliderR.setMaximum(100)
        self.sliderR.setValue(100)
        self.sliderR.valueChanged.connect(self.update_image)

        self.sliderG.setMinimum(0)
        self.sliderG.setMaximum(100)
        self.sliderG.setValue(100)
        self.sliderG.valueChanged.connect(self.update_image)

        self.sliderB.setMinimum(0)
        self.sliderB.setMaximum(100)
        self.sliderB.setValue(100)
        self.sliderB.valueChanged.connect(self.update_image)

        self.load_button.clicked.connect(self.load_image)
        self.save_button.clicked.connect(self.save_image)
        self.save_button.setEnabled(False)

    def load_image(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Load Image", "", "Image Files (*.png *.jpg *.bmp)",
                                                   options=options)
        if file_path:
            self.image_compressor.load_image(file_path)
            self.update_image()

    def update_image(self):
        if self.image_compressor.file_path is None:
            print("No image loaded")
            return

        compression_factors = [
            self.image_compressor.get_size_img(self.sliderR.value()),
            self.image_compressor.get_size_img(self.sliderG.value()),
            self.image_compressor.get_size_img(self.sliderB.value())
        ]

        self.image_compressor.compress_image(compression_factors)
        self.image_compressor.compressed_image.save(
            os.getcwd() + "/temp" + os.path.splitext(self.image_compressor.file_path)[1])

        file_size_ratio = self.image_compressor.get_file_size_ratio()
        self.size.setText(str(round(file_size_ratio, 1)))


        # Вычисляем и отображаем процент изменения размера
        size_difference_percentage = self.image_compressor.get_size_difference_percentage()
        self.proc_compress.setText(f"{round(size_difference_percentage, 2)}%")  # Отображаем разницу

        self.show_image(self.image_compressor.compressed_image)
        self.save_button.setEnabled(True)

    def show_image(self, image):
        pixmap = QPixmap.fromImage(ImageQt(image))
        self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.KeepAspectRatio))

    def save_image(self):
        if self.image_compressor.compressed_image is not None:
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", "", options=options)
            if file_name:
                self.image_compressor.compressed_image.save(
                    file_name + os.path.splitext(self.image_compressor.file_path)[1])
