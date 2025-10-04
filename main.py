try:
	from Pyside2 import QtCore, QtGui, QtWidgets
	from shoboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui

ROOT_RESOURCE_DIR = 'C:/Users/ladch/OneDrive/maya/2024/scripts/myStyleTool/picture'

class MyStyleToolDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setWindowTitle('❄️My Boo☃️')
		self.resize(350,200)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet('background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B2DAFF, stop:1 #F9F4A2);')

		self.imageLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/02.jpg")
		scaled_pixmap = self.imagePixmap.scaled(
			QtCore.QSize(128,128),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation
		)

		self.imageLabel.setPixmap(scaled_pixmap)
		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)

		self.mainLayout.addWidget(self.imageLabel)

		self.nameLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.nameLayout)
		self.nameLabel = QtWidgets.QLabel('🪼NAME: ')
		self.nameLabel.setStyleSheet(
			'''
				QLabel {
					background-color: #B2DAFF;
					color: Brown;
					font-size: 16px;
					font-family: DIN Medium;
					font-weight: Medium;
				}
			'''
		)
		self.nameLineEdit = QtWidgets.QLineEdit()
		self.nameLineEdit.setStyleSheet(
			'''
				QlineEdit {
					color: navy;
					background-color: #B2DAFF;
					font-family: DIN Medium;
					border-radius: 10px;					
					font-weight: bold;
				}
			'''
		)
		self.nameLayout.addWidget(self.nameLabel)
		self.nameLayout.addWidget(self.nameLineEdit)

		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)
		self.createButton = QtWidgets.QPushButton('💚CREATE: ')
		self.createButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #95FCB4;
					color: white;
					border-radius: 10px;
					font-size: 16px;
					font-family: DIN Medium;
					font-weight: bold;
				}
				QPushButton:hover {
					background-color: #8DCBFA;
				}
				QPushButton:pressed {
					background-color: #D084FA;
				}
			'''
		)
		self.cancelButton = QtWidgets.QPushButton('⛔CANCEL: ')
		self.cancelButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #FA7DC6;
					color: white;
					border-radius: 10px;
					font-size: 16px;
					font-family: DIN Medium;
					font-weight: bold;
				}
				QPushButton:hover {
					background-color: #8DCBFA;
				}
				QPushButton:pressed {
					background-color: #FFBC85;
				}
			'''
		)

		self.buttonLayout.addWidget(self.createButton)
		self.buttonLayout.addWidget(self.cancelButton)

		self.mainLayout.addStretch()

def run():
    global ui

    try:
        ui.close()
    except:
        pass

    ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
    ui = MyStyleToolDialog(parent=ptr)
    ui.show()