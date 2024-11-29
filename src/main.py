import sys
from PySide6 import  QtWidgets
from widgets.image_selecter import ImageSelecter
from widgets.image_viewer import ImageViewer

class MainWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWidget()
    layout = QtWidgets.QVBoxLayout()
    image_viewer = ImageViewer()
    image_selecter = ImageSelecter(image_viewer.setImage)
    layout.addWidget(image_viewer)
    layout.addWidget(image_selecter)
    window.central_widget.setLayout(layout)
    window.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())