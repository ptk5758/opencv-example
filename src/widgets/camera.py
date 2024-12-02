import cv2
import threading
import time
from PySide6 import QtWidgets, QtCore, QtGui
from widgets.image_viewer import ImageViewer
class Camera(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.capture_button = QtWidgets.QPushButton("Capture")
        self.capture_button.clicked.connect(self.stopLive)
        self.camera = cv2.VideoCapture(1)
        self.camera.read()
        self.camera_frame_width = self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.camera_frame_height = self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
        
        # Image Viewer
        self.image_viewer = ImageViewer()

        self.camera_worker = CameraWorker(self.camera)
        self.camera_worker.update_signal.connect(self.viewImage)

        self.initUI()

        self.camera_worker.start()

    def initUI(self):
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.image_viewer)
        layout.addWidget(self.capture_button)
        self.setLayout(layout)

    @QtCore.Slot()
    def viewImage(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.image_viewer.setImage(image)

    @QtCore.Slot()
    def stopLive(self):
        self.camera_worker.state = False
        self.camera_worker.wait()
        self.camera_worker.quit()

class CameraWorker(QtCore.QThread):
    update_signal = QtCore.Signal(object)

    def __init__(self, camera):
        super().__init__()
        self.camera = camera
        self.state = True

    def run(self):
        while self.state :
            flag, image = self.camera.read()
            if not flag :
                break
            self.update_signal.emit(image)
            time.sleep(0.03)