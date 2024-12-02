import cv2
import threading
import time
from PySide6 import QtWidgets, QtCore, QtGui
from widgets.image_viewer import ImageViewer
class Camera(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.capture_button = QtWidgets.QPushButton("Capture")
        self.capture_button.clicked.connect(self.capture)
        self.camera = cv2.VideoCapture(1)
        self.camera_frame_width = self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.camera_frame_height = self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
        
        # Image Viewer
        self.image_viewer = ImageViewer()

        # Video 부분
        self.video = Video()
        self.video.start()

        self.initUI()

    def initUI(self):
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.image_viewer)
        layout.addWidget(self.capture_button)
        self.setLayout(layout)

    @QtCore.Slot()
    def capture(self):
        state, image = self.camera.read()
        if state :
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            self.image_viewer.setImage(image)
            # h, w, c = image.shape
            # qt_image = QtGui.QImage(image.data, w, h, w * c, QtGui.QImage.Format.Format_RGB888)
            # pixmap = QtGui.QPixmap.fromImage(qt_image)
            # self.label.setPixmap(pixmap)


class Video(threading.Thread):
    def run(self):
        print("시작..")
        time.sleep(3)
        print("종료.")