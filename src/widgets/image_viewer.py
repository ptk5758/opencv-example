import cv2
from PySide6 import QtWidgets, QtGui

class ImageViewer(QtWidgets.QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.image_path = image_path
        self.label = QtWidgets.QLabel("이미지를 선택하여 주세요")
        self.initUI()

    def initUI(self):
        layout = QtWidgets.QVBoxLayout()
        image = cv2.imread(self.image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image.shape
        q_img = QtGui.QImage(image.data, width, height, QtGui.QImage.Format.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(q_img)
        self.label.setPixmap(pixmap)
        self.label.resize(width, height)
        layout.addWidget(self.label)
        self.setLayout(layout)