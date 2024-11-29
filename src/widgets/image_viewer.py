import cv2
from PySide6 import QtWidgets, QtGui, QtCore

class ImageViewer(QtWidgets.QWidget):
    def __init__(self, image_path=None):
        super().__init__()
        self.label = QtWidgets.QLabel("이미지를 선택하여 주세요")
        self.initUI()
        if image_path:
            self.setImage(image_path)

    def initUI(self):
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    @QtCore.Slot()
    def setImage(self, path):

        """이미지를 로드하여 QLabel에 표시합니다."""
        image = cv2.imread(path)
        # print(image.shape) # B, G, R
        if image is None:
            print(f"Error: Unable to load image from path: {path}")
            self.label.setText("이미지 로드 실패")
            self.label.setPixmap(QtGui.QPixmap())  # 기존 이미지를 초기화
            return
        # print(1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # print(2)
        height, width, channel = image.shape
        q_img = QtGui.QImage(image.data, width, height, width * 3, QtGui.QImage.Format.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(q_img)
        self.label.setPixmap(pixmap)
        self.label.resize(width, height)
