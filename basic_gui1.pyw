#!/usr/bin/env python

import sys
from sample_main import *
from PyQt4.QtGui import *

class MyGui(QMainWindow):
	def __init__(self,parent=None):
		QWidget.__init__(self,parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'),self.ClearField)
		QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL('clicked()'),self.PopMessage)
		QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL('clicked()'),self.ExitMessageBox)
				
	def ClearField(self):
		self.ui.lineEdit.clear()
		self.ui.lineEdit_2.clear()
		
	def PopMessage(self):
		msgBox = QWidget(self)
		res = QMessageBox.information(msgBox, "Message", "Hello!")
		msgBox.show()
	
	def ExitMessageBox(self):
		res = QMessageBox.question(self, 'Message', "Are you sure you want to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)			
		if res == QMessageBox.Yes:
			self.close()
		else:
			pass

if __name__ == '__main__':
	app = QApplication(sys.argv)

MyApp = MyGui()
MyApp.show()
sys.exit(app.exec_())
