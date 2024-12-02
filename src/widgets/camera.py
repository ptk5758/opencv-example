import cv2
from PySide6 import QtWidgets, QtCore, QtGui
class Camera(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel("Image...")
        self.capture_button = QtWidgets.QPushButton("Capture")
        self.capture_button.clicked.connect(self.capture)
        self.camera = cv2.VideoCapture(1)
        self.camera_frame_width = self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.camera_frame_height = self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.initUI()

    def initUI(self):
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.capture_button)
        self.setLayout(layout)

    @QtCore.Slot()
    def capture(self):
        state, image = self.camera.read()
        print(state)
        if state :
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            h, w, c = image.shape
            qt_image = QtGui.QImage(image.data, w, h, w * c, QtGui.QImage.Format.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(qt_image)
            self.label.setPixmap(pixmap)
