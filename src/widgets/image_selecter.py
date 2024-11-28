import pathlib
from PySide6 import QtWidgets, QtCore
from lib.util import getDocumentPath
class ImageSelecter(QtWidgets.QWidget):
    def __init__(self, listener):
        super().__init__()
        self.listener = listener
        
        self.button = QtWidgets.QPushButton("Image Select..")
        self.button.clicked.connect(self.fileSelect)
        self.initUI()

    def initUI(self):
        layout = QtWidgets.QVBoxLayout()

        self.button.setStyleSheet(
            "color : blue; font-size : 24px"
        )
        layout.addWidget(self.button)    

        self.setLayout(layout)


    @QtCore.Slot()
    def fileSelect(self):        
        path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "이미지 선택",
            getDocumentPath(),
            "Image (*.jpg *.png *.jpeg)"
        )
        self.listener(path)